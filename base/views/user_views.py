from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from base.serializers import ProductSerializer, UserSerializer, UserSerializerwithToken
# from .products import products

# for customizing jwt token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Added custom data in jwt token
        serializer = UserSerializerwithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

# changing default serializer behaviour, in base/url we will get this customized user data
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# for user profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# register user
@api_view(['POST'])
def userRegister(request):
    data = request.data
    try:
        user = User.objects.create(
        first_name = data['name'],
        username = data['email'],
        email = data['email'],
        password = make_password(data['password'])
        )
        serializer = UserSerializerwithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'details': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

# for all users
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
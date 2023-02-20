from django.shortcuts import render
from django.http import JsonResponse

from base.models import Product
from base.serializers import ProductSerializer
from .products import products

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',

        'api/products/upload/',

        'api/products/<id>/reviews/',

        'api/products/top/',
        'api/products/<id>',
        
        'api/products/delete/<id>/',
        'api/products/<update>/<id>/',
    ]
    return Response(routes)

# for all products
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# for single product
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
urlpatterns = [
    path('users/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    # means there will be dynamic data, slug/id, for single product
    path('products/<str:pk>', views.getProduct, name='product'),
]

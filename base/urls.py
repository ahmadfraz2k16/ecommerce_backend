from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    # means there will be dynamic data, slug/id, for single product
    path('products/<str:pk>', views.getProduct, name='product'),
]

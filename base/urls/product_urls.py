from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),
    # means there will be dynamic data, slug/id, for single product
    path('<str:pk>', views.getProduct, name='product'),
]

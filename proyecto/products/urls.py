from django.contrib import admin
from django.urls import path ,include
from products.views import create_product,list_products,list_categorys,create_category

urlpatterns = [
    path('create-product/',create_product),
    path('list-products/',list_products),
    path('list-categorys/',list_categorys),
    path('create-category/',create_category)
]
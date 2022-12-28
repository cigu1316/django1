from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products,Categorys


def create_product(request):
    new_product = Products.objects.create(name ='coca cola 2 litro', price = 400,stock = False)
    print(new_product)
    return HttpResponse("se creo el nuevo producto")

def list_products(request):
    all_products = Products.objects.all()
    print(all_products)
    context = {
        'products':all_products,
    }
    return render(request,'list_products.html',context=context) 

def create_category(request,name):
    Categorys.objects.create(name=name)
    return HttpResponse('categoria creada')

def list_categorys(request):
    all_categorys=Categorys.objects.all()
    context = {
        'categorys':all_categorys,
    }
    return render(request,'list_categorys.html',context=context) 

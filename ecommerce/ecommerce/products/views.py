from multiprocessing import context
from django.shortcuts import render
from products.models import Products
from products.forms import Formulario_productos


def create_product(request):

    if request.method == 'POST':
        pass
        # productos = Products.objects.all()
        # context = {}
        # if len(productos) >= 3:
        #     new_product = Products.objects.create(name = 'Coca cola 1l', price = 350, stock = 10)
        #     context = {
        #         'new_product':new_product
        #     }
    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form':form}
        return render(request, 'products/new_product.html', context=context)

def list_products(request):
    products = Products.objects.all()
    print(len(products))
    context = {
        'products':products
    }
    return render(request, 'products/products_list.html', context=context)

def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Products.objects.create(name = request.POST['name'])
    return render(request, 'products/primer_formulario.html', context={})

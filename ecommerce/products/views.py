from multiprocessing import context
from django.shortcuts import redirect, render
from products.models import Products
from products.forms import Formulario_productos


def create_product(request):
    
    if request.method == 'POST':
        form = Formulario_productos(request.POST)

        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                stock = form.cleaned_data['stock']
            )
            
            return redirect(list_products)

    elif request.method == 'GET':
        form = Formulario_productos()
        context = {'form':form}
        return render(request, 'products/new_product.html', context=context)

def update_product(request, pk):
    if request.method == 'POST':
        form = Formulario_productos(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.save()

            return redirect(list_products)


    elif request.method == 'GET':
        product = Products.objects.get(id=pk)

        form = Formulario_productos(initial={
                                        'name':product.name,
                                        'price':product.price, 
                                        'description':product.description,
                                        'stock':product.stock})
        context = {'form':form}
        return render(request, 'products/update_product.html', context=context)





def list_products(request):
    products = Products.objects.all() #Trae todos
    context = {
        'products':products
    }
    return render(request, 'products/products_list.html', context=context)

def primer_formulario(request):
    print(request.method)
    if request.method == 'POST':
        Products.objects.create(name = request.POST['name'])
    return render(request, 'products/primer_formulario.html', context={})

def search_products(request):
    search = request.GET['search']
    products = Products.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'products':products}
    return render(request, 'products/search_product.html', context=context)

def delete_product(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(pk=pk)
        context = {'product':product}
        return render(request, 'products/delete_product.html', context=context)
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_products)


#Products.objects.get(id=1) #Trae solo el objeto que cumpla la condicion
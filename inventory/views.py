from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def singup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = UserForm()
    if request == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    return render(request, 'singup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def inventory(request):
    return render(request, 'inventory.html')

#Pendiente de hacerlo funcionar con el nombre del usuario y no con el id
@login_required
def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {
        'products': products
        })


@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'new_product.html', {'form': form})


@login_required
def modify_product(request):
    return render(request, 'modify_product.html')


@login_required
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers.html', {
        'suppliers': suppliers
        })


@login_required
def new_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    return render(request, 'new_supplier.html', {'form': form})


@login_required
def modify_supplier(request):
    return render(request, 'modify_supplier.html')


@login_required
def categories(request):
    return render(request, 'categories.html')


@login_required
def new_category(request):
    return render(request, 'new_category.html')


@login_required
def modify_category(request):
    return render(request, 'modify_category.html')


@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {
        'users': users})


@login_required
def modify_user(request):
    return render(request, 'modify_user.html')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password1']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('password is do not match')


def login(request):
    return render(request, 'login.html')


def inventory(request):
    return render(request, 'inventory.html')


def products(request):
    return render(request, 'products.html')


def new_product(request):
    return render(request, 'new_product.html')


def modify_product(request):
    return render(request, 'modify_product.html')


def suppliers(request):
    return render(request, 'suppliers.html')


def new_supplier(request):
    return render(request, 'new_supplier.html')


def modify_supplier(request):
    return render(request, 'modify_supplier.html')


def categories(request):
    return render(request, 'categories.html')


def new_category(request):
    return render(request, 'new_category.html')


def modify_category(request):
    return render(request, 'modify_category.html')


def users(request):
    return render(request, 'users.html')


def modify_user(request):
    return render(request, 'modify_user.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = UserForm()
    if request == 'GET':
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/',)
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/')
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

@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def inventory(request):
    return render(request, 'inventory.html')

@login_required(login_url='/')
def products(request):
    return render(request, 'products.html')

@login_required(login_url='/')
def new_product(request):
    return render(request, 'new_product.html')

@login_required(login_url='/')
def modify_product(request):
    return render(request, 'modify_product.html')

@login_required(login_url='/')
def suppliers(request):
    return render(request, 'suppliers.html')

@login_required(login_url='/')
def new_supplier(request):
    return render(request, 'new_supplier.html')

@login_required(login_url='/')
def modify_supplier(request):
    return render(request, 'modify_supplier.html')

@login_required(login_url='/')
def categories(request):
    return render(request, 'categories.html')

@login_required(login_url='/')
def new_category(request):
    return render(request, 'new_category.html')

@login_required(login_url='/')
def modify_category(request):
    return render(request, 'modify_category.html')

@login_required(login_url='/')
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required(login_url='/')
def modify_user(request):
    return render(request, 'modify_user.html')

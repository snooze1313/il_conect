"""ilconect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('home/', views.home),
    path('singup/', views.singup),
    path('inventory/', views.inventory),
    path('products/', views.products),
    path('products/new/', views.new_product),
    path('products/modify/', views.modify_product),
    path('suppliers/', views.suppliers),
    path('suppliers/new/', views.new_supplier),
    path('suppliers/modify/', views.modify_supplier),
    path('categories/', views.categories),
    path('categories/new/', views.new_category),
    path('categories/modify/', views.modify_category),
    path('users/', views.users),
    path('users/modify/', views.modify_user),
]

from django.shortcuts import render, redirect
from home.models import *
from home.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from home.forms import *

# Create your views here.

@login_required(login_url='login')
def home(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images, 'cats': cats}


    return render(request, 'home.html', data)


@login_required(login_url='login')
def show_category_page(request,cid):
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}


    return render(request, 'home.html', data)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for" + user)
                return redirect('login')

        data = {'form':form}
        return render(request, 'register.html', data)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('home')

            else:
                messages.info(request, 'Username or Password is incorrect')

        data = {}
        return render(request, 'login.html', data)

def logoutUser(request):
    logout(request)
    return redirect('login')



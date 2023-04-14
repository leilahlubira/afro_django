from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User_account
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    username = 'Leilah'
    gender = 'Female'
    return render(
        request,
        'index.html', 
        {'pr_title': pr_title, 'username':username, 'gender':gender}
    )

def register(request):
    return render(request, 'register.html')

def registration(request):
    username = request.POST['username']
    email = request.POST['user_email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details=[
            username,email,password,gender]
    
    print(user_details)
    if User.objects.filter(username=username).first():
        print('Username already exists')
        return render(request, 'login.html')
    else:
        user = User.objects.create_user(username, email, password)
        return render(request, 'login.html')

def login_user(request):
    username = request.POST['username']
    pwd = request.POST['password']
    if User.objects.filter(username=username):
        print('This username exists.')
        logged_user = authenticate(request, username=username, password=pwd)
        if logged_user is not None:
            #Here we are logging in the user
            auth_login(request, logged_user)
            print(username + ' '+ 'Logged in successfully.')
            return redirect('index')
        else:
            #handling a scenario when authentication has failed.
            return render(request, 'login.html')
    else:
        print('User credentials do not exist.')
        return render(request, 'login.html')
    
def login_page(request):
    return render('login.html')

    
    
    
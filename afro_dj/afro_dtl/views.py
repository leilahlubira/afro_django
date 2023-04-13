from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

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
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details=[
            username,email,password,gender
        ]
    print(user_details)
    return render(request, 'index.html', {'username': username})
   



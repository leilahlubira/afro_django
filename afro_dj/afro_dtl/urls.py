from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('login_user', views.login_user, name = 'login_user'),
    path('login_page', views.login_page, name = 'login_page'),
    path('logout_user', views.logout_user, name = 'logout_user'),
    path('user_form', views.user_form, name='user_form'),
    path('userforminfo', views.userforminfo, name='userforminfo'),
    path('capture_message', views.capture_message, name='capture_message'),
    
    
]

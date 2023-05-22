from django.db import models

# Create your models here.
# Creating a custom user model instead of django's out the box.
class User_account(models.Model):
    username = models.CharField(max_length=22 )
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now=True)
    
#new chatbox model
class ChatBox(models.Model):
    messenger = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=200, blank=True)


    
#test model
class User_form_model(models.Model):
    name =  models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    occupation = models.CharField(max_length=1000)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name
    
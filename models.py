from django.db import models
class LoginData(models.Model):
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

class SignupData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)
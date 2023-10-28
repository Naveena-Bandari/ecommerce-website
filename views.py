from django.shortcuts import render,redirect
from .models import LoginData

def home(request):
    return render (request,'homepage.html')
def gallery(request):
    return render (request,'gallerypage.html')
def login(request):
    if request.method=='GET':
      return render (request,'login.html')
    else:
        LoginData(
        user_name=request.POST.get('uname'),
        email=request.POST.get('email'), 
        password=request.POST.get('password'),
        ).save()
def signup(request):
    if request.method=='GET':
        return render (request,'signup.html')
    else:
        SignupData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        email=request.POST.get('email'), 
        password=request.POST.get('password'),
        ).save()
def clothes(request):
    return render (request,'clothes.html')
def toys(request):
    return render (request,'toys.html')
def shampoo(request):
    return render (request,'shampoo.html')
def wipes(request):
    return render (request,'wipes.html')
def nailclippers(request):
    return render (request,'nailclippers.html')
def fleacombs(request):
    return render (request,'fleacombs.html')
def desheddingbrushes(request):
    return render (request,'desheddingbrushes.html')

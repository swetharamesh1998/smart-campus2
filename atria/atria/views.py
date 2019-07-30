from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home/homepage.html')

def login(request):
    return render(request,'home/login.html')

def collegemap(request):
    return render(request,'home/collegemap.html')

def attendence(request):
    return render(request,'home/attendence.html')

def marks(request):
    return render(request,'home/marks.html')

def registration(request):
    return render(request,'home/registration.html')

def registrationcont(request):
    return render(request,'home/registration2.html')

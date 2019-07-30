from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
import sqlite3
from django.core.exceptions import ValidationError
from .models import details
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def homepage(request):
    return render(request, 'home/homepage.html')


def login(request):
    return render(request, 'home/login.html')


def collegemap(request):
    return render(request, 'home/collegemap.html')


def attendence(request):
    return render(request, 'home/attendence.html')


def marks(request):
    return render(request, 'home/marks.html')


def registration(request):
    return render(request, 'home/registration.html')

@csrf_exempt
def registration2(request):
    f2 = forms.RegistrationForm()
    if(request.method=="POST"):
        f2 = forms.RegistrationForm(request.POST)
        if(f2.is_valid()):
            f3 = f2.cleaned_data
            conn = sqlite3.connect('db.sqlite3')
            cur = conn.connect()
            cur.execute('select status from student_entry where passcode=?',(f3['passcode']))
            result =cur.fetchone()
            if(result is None):
                f3["display"]="Invalid User"
            else:
                result2=''.join(result)
                if(result2=='P'):
                    return(render(request,'home/registration2.html'))
                else:
                    f3["display"]="Registration Already Done"
        return(render(request,'home/registration.html',{'form ':f3}))


def registration_details(request):
    f2=forms.RegistrationDetails()
    if request.method=="POST":
        f2=forms.RegistrationDetails(request.POST)
        if(f2.is_valid()):
            f3=f2.cleaned_data
            conn=sqlite3.connect('db.sqlite3')
            cur=conn.connect()
            cur.execute('insert into student_details (usn,name,ph_no,email,dept,address,blood_group,parent_name,parent_phno) values (?,?,?,?,?,?);',(f3['usn'],f3['name'],f3['ph_no'],f3['email'],f3['dept'],f3['address'],f3['blood_group'],f3['parent_name'],f3['parent_phno']))  
            conn.commit()
        else :
            raise ValidationError("Enter the appropriate details")
    return(render(request,'home.html',{'form':f2}))
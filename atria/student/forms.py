from django import forms
from .models import students


class RegistrationForm(forms.Form):
    password = forms.CharField(max_length=8,min_length=8)
    invalidUser = forms.CharField(widget = forms.HiddenInput)


class RegistrationDetails(forms.Form):
    usn=forms.CharField(max_length=10,min_length=10)
    name=forms.CharField(max_length=50)
    ph_no=forms.CharField(max_length=10,min_length=10)
    email=forms.EmailField()
    dept=forms.CharField()
    address=forms.Textarea()
    blood_group= forms.CharField(max_length=3)
    father_name=forms.CharField(max_length=50)
    father_phno=forms.CharField(max_length=10,min_length=10)

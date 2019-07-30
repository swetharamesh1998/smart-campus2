from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class students(models.Model):
    usn1 = models.CharField(primary_key=True, max_length=10, validators=[MinLengthValidator(10, message=None)])
    name = models.CharField(blank=False, max_length=50)


class details(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    address = models.TextField()
    ph_no = models.CharField(max_length=10, validators=[MinLengthValidator(10, message=None)])
    email = models.EmailField(max_length=254,default="Enter Email")
    dept = models.CharField(max_length=3,validators=[MinLengthValidator(2,message=None)])
    blood_group = models.CharField(max_length=3)
    parent_name=models.CharField(max_length=50)
    parent_phno=models.CharField(max_length= 10,validators =[MinLengthValidator(10,message=None)])



class entry(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    passcode = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    status = models.CharField(max_length=1, default='P')


class Authenticate(models.Model):
    uid = models.ForeignKey(entry, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    pwd = models.TextField()


class events(models.Model):
    mid = models.TextField(max_length=17, primary_key=True)
    EventName = models.TextField()


class CheckIn(models.Model):
    uid = models.ForeignKey(entry, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    checkInTime = models.DateTimeField(auto_now=True)
    mid = models.ForeignKey(events, on_delete=models.CASCADE)


class SubID(models.Model):
    subid = models.CharField(primary_key=True, max_length=8)


class Subject(models.Model):
    subid = models.ForeignKey(SubID, on_delete=models.CASCADE)
    subname = models.CharField(max_length=30)
#staffname = models.ForeignKey(staff.S_Name, on_delete=models.CASCADE)

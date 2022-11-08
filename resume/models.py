from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Resume2(models.Model):
    name=models.CharField(max_length=100)
    #date_of_birth=models.DateField()
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    address=models.TextField(max_length=100)
    summary=models.TextField(max_length=100)
    highschool=models.CharField(max_length=100)
    seniorschool=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    previous_work=models.TextField(max_length=400)
    skills=models.TextField(max_length=400)
    fathername=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(max_length=400)

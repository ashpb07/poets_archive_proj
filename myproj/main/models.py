from django.db import models

# Create your models here.
class Member(models.Model):
    username=models.CharField(max_length=50)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)

    email=models.CharField( max_length=50)
    pass1=models.CharField(max_length=50)

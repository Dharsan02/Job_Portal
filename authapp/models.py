from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  mobile_no=models.CharField(max_length=10,unique=True)
  location=models.CharField(max_length=50,null=True)
  industry_type=models.CharField(max_length=50,null=True)
  

# Create your models here.

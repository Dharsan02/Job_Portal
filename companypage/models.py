from django.db import models
from internpage.models import *

class Companypost(models.Model):
  jobpost=models.ForeignKey(JobPost,on_delete=models.CASCADE)
  


# Create your models here.


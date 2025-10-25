from django.db import models

from authapp.models import *

class JobPost(models.Model):
  role=models.CharField(max_length=100)
  company_name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  description=models.TextField()
  responsiablity=models.TextField(null=True)
  experience=models.CharField(max_length=100,null=True)
  skills=models.CharField(max_length=100)
  date_posted=models.DateField(null=True,blank=True)
  reciver_email=models.EmailField(null=True)

  def __str__(self):
    return self.company_name
class Application(models.Model):
  job=models.ForeignKey(JobPost,on_delete=models.CASCADE)
  userdata=models.ForeignKey(User,on_delete=models.CASCADE)
  resume=models.FileField(upload_to='resumes/')
  location=models.CharField(max_length=100)
  experience=models.CharField(max_length=50)

class Candidate_profile(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  resume=models.FileField(upload_to='resumes/')
  location=models.CharField(max_length=100)
  experience=models.CharField(max_length=50)
  skills=models.TextField()
  education=models.CharField(max_length=200)
  projects=models.CharField(max_length=200,null=True)
  summary=models.TextField(null=True)
# Create your models here.

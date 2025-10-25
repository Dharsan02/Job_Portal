from django.shortcuts import render
from django.views.generic import DetailView,CreateView,ListView,TemplateView
from .models import *

class Createjobpost(CreateView):
  model=JobPost
  fields="__all__"
  template_name = "Jobpost.html"
  success_url="company_home"
class Homepage(TemplateView):
  template_name="company_home.html"





# Create your views here.

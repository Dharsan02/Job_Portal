from django.forms import ModelForm
from .models import *
from authapp.models import *

class Company_form(ModelForm):
  class Meta:
    model=User
    fields=''

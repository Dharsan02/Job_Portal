from django.urls import path
from .views import *


urlpatterns=[
  path('job_post/',Createjobpost.as_view(),name='job_post'),
  path('hire/',Homepage.as_view(),name='hire')
]

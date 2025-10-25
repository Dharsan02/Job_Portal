from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns=[
  path('home/',home,name='home'),
  path('read/<int:id>',read,name='read'),
  path('apply/<int:jobid>',application,name='apply'),
  path('profileview/',profileview,name='profileview'),
  path('updateprofile/<int:userid>/',profileupdated,name="profileupd"),
  path('',homepage,name="internapp")
]



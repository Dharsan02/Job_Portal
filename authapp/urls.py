from django.urls import path
from .views import *
urlpatterns=[
  path('signup/',signup,name='signup'),
  path('login/',login,name='login'),
  path('logut/',logout,name='logout'),
  path('company_signup/',company_signup,name='company_signup'),
  path('company_login/',company_login,name='company_login'),
  path('company_logout/',company_logout,name='company_logout')
]
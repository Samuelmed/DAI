# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='mi_form'),
  path('test_template', views.test_template, name='test_template'),
  
]
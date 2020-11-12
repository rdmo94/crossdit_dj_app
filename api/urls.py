# ./bookstore_app/api/urls.py

from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getReading', views.getReading)
]
# map urls to view functions in views.py

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello)
]

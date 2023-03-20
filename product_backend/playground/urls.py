# map urls to view functions in views.py

from django.urls import path
from . import views

urlpatterns = [
    path('input/',views.my_view, name='my_view')
]

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# view func takes a req and gives a response
# a basic request handler

def say_hello(request):
    #return HttpResponse('Hello World')
    return render(request, 'input.html')

def return_data(request):
    a = 3
    b = 4
    return HttpResponse(float(a+b))
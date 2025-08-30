from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def say_hello(request):
     x=1
     y=3
     return render( request , 'hello.html')
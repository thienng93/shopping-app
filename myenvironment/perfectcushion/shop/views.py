from django.shortcuts import render
from django.http import HttpResponse        

def index(request): 
    text_var = 'This is my first django web app app web page'
    return HttpResponse(text_var)
# Create your views here.

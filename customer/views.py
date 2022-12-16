from email.mime import image
from urllib import request
from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request,'the/new.html')

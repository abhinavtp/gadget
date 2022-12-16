from email.mime import image
from urllib import request
from django.shortcuts import render

# Create your views here.
def loginss(request):
    return render(request,'has/loginss.html')
def userlogin(request):
    return render(request,'has/userlogin.html')
def index(request):
    return render(request,'has/index.html')    




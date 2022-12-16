from django.shortcuts import render
from login.models import Login
# Create your views here.
from engineer.models import Engineer

def register(request):
    if request.method=="POST":
        obj=Engineer()
        obj.name=request.POST.get('nm')
        obj.address = request.POST.get('addrs')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phn')
        obj.password=request.POST.get('password')
        obj.save()
        o = Login()
        o.username = request.POST.get('nm')
        o.password = request.POST.get('password')
        o.type='service_engineer'
        o.u_id=obj.e_id
        o.save()
    return render(request,'engineer/engineer_register.html')
from django.shortcuts import render
from customer.models import Customer
from login.models import Login
# Create your views here.
def register(request):
    if request.method =="POST":
        obj=Customer()
        obj.name=request.POST.get('nm')
        obj.address=request.POST.get('addrs')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phn')
        obj.password=request.POST.get('password')
        obj.save()
        o=Login()
        o.username=request.POST.get('nm')
        o.password=request.POST.get('password')
        o.type='custemer'
        o.u_id=obj.c_id
        o.save()
    return render(request,'customer/customer_registration.html')
def manage(request):
    obj=Customer.objects.all()
    context={
       'details':obj
    }
    return render(request,'customer/manage_customer.html',context)
def approve(request,idd):
    obj=Customer.objects.get(c_id=idd)
    obj.status="accepted"
    obj.save()
    return manage(request)
def reject(request,idd):
    obj=Customer.objects.get(c_id=idd)
    obj.status="reject"
    obj.save()
    return manage(request)


from django.http import HttpResponse
from rest_framework.views import APIView,Response
from customer.serializer import android
# import datetime
class customer_view(APIView):
    def get(self,request):
        ob=Customer.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
     if request.method =="POST":
        obj=Customer()
        obj.name=request.data['name']
        obj.address=request.data['address']
        obj.email=request.data['email']
        obj.phone=request.data['phone']
        obj.password=request.data['password']
        obj.status='pending'
        obj.save()
        return HttpResponse('Success')
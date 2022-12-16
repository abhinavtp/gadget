from django.shortcuts import render

# Create your views here.
from service.models import Service
def add(request):
    if request.method=="POST":
        obj=Service()
        obj.service=request.POST.get('service')
        obj.details=request.POST.get('details')
        obj.u_id=request.session["uid"]
        obj.save()
    return render(request,'service/add_service.html')
def view_service(request):
    object=Service.objects.all()
    context={
        'objval':object
    }
    return render(request,'service/c_view_service.html',context)
def request(request,idd):
    obj=Service.objects.get(service_id=idd)
    obj.status = "requested"
    obj.save()
    return render(request,'service/view_service.html')


def manage(request):
    object=Service.objects.all()
    context={
        'details':object
    }
    return render(request,'service/manage_service.html',context)
def approve(request,idd):
    obj=Service.objects.get(service_id=idd)
    obj.status="accepted"
    obj.save()
    return manage(request)
def reject(request,idd):
    obj=Service.objects.get(service_id=idd)
    obj.status="reject"
    obj.save()
    return manage(request)
def rqst(request,idd):
    object=Service.objects.get(service_id=idd)
    context={
        'objval':object
    }
    return render(request, 'service/service_request.html', context)
def rqst_view(request):
    obj=Service.objects.all()
    context={
        'objval':obj
    }
    return render(request,'service/view_service.html',context)
def r_view(request):
    object=Service.objects.all()
    context={
        'msg':object
    }
    return render(request, 'request/view_request.html', context)
def add_updte(request,abc):
    if request.method == "POST":
        obj = Service.objects.get(service_id=abc)
        obj.status = request.POST.get('staus')
        obj.save()
    return render(request,'service/update_service.html')
def update(request):
    obj=Service.objects.all()
    context={
        'update':obj
    }
    return render(request, 'service/update_service.html', context)




from django.http import HttpResponse
from rest_framework.views import APIView,Response
from service.serializer import android
# import datetime
class service_view(APIView):
    def get(self,request):
        ob=Service.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob= Service()
        ob.service_id=request.data['service_id']
        ob.u_id=request.data['u_id']
        ob.service=request.data['service']
        ob.details=request.data['details']
        ob.status='pending'
        ob.save()
        return HttpResponse('success')


from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
from complaint.models import Complaint


def add(request):
    if request.method == "POST":
        obj = Complaint()
        obj.complaint = request.POST.get('complaint')
        obj.date = datetime.date.today()
        obj.time = datetime.datetime.now()
        obj.reply = "pending"
        obj.save()
    return render(request, 'complaint/add_complaint.html')


def manage(request):
    obj = Complaint.objects.all()
    context = {
        'objval': obj
    }
    return render(request, 'complaint/view_complaint.html', context)


# def approve(request,abc):
#     obj=Complaint.objects.get(comp_id=abc)
#     obj.status="accepted"
#     obj.save()
#     return view(request)
# def reject(request,abc):
#     obj=Complaint.objects.get(comp_id=abc)
#     obj.status="reject"
#     obj.save()
#     return view(request)
def view(request):
    obj = Complaint.objects.filter(reply="pending")
    context = {
        'details': obj
    }
    return render(request, 'complaint/view_complaint.html', context)


def view_reply(request):
    obj = Complaint.objects.all()
    context = {
        'rplyy': obj
    }
    return render(request, 'complaint/view_reply.html', context)


def post_reply(request, abc):
    if request.method == "POST":
        obj = Complaint.objects.get(comp_id=abc)
        obj.reply = request.POST.get('reply')
        obj.save()
    return render(request, 'complaint/reply.html')


from django.http import HttpResponse
from rest_framework.views import APIView, Response
from complaint.serializer import android
import datetime


class complaint_view(APIView):
    def get(self, request):
        ob = Complaint.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = Complaint()
        ob.u_id = request.data['u']
        ob.date = datetime.datetime.today()
        ob.complaint = request.data['complaint']
        ob.time = datetime.datetime.today()
        ob.reply = 'pending'
        ob.save()
        return HttpResponse('POST')

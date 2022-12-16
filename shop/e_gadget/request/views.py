from django.shortcuts import render

# Create your views here
from request.models import RequestService
def request(request):
    object = RequestService.objects.all()
    context = {
        'msg': object
    }
    return render(request,'request/view_request.html',context)
# def update(request,abc):
#     a=RequestService.objects.get(requst_id=abc)
#     if request.method=="POST":
#         if __name__ == '__main__':
#             a.status=request.POST.get('')




from django.http import HttpResponse
from rest_framework.views import APIView,Response
from request.serializer import android
# import datetime
class request_view(APIView):
    def get(self,request):
        ob=RequestService.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob= RequestService()
        ob.service_id=request.data['service']
        ob.u_id=request.data['u']
        ob.requst_id=request.data['requst_id']
        ob.status='pending'
        ob.save()
        return HttpResponse('ok')
from django.shortcuts import render

# Create your views here.
from rating.models import Rating
def add(request):
    if request.method=="POST":
        obj=Rating()
        obj.rating=request.POST.get('rating')
        obj.u_id="1"
        obj.save()
    return render(request,'rating/add_rating.html')
def view(request,):
    obj = Rating.objects.all()
    context = {
        'details': obj
    }
    return render(request,'rating/view_rating.html',context)



from django.http import HttpResponse
from rest_framework.views import APIView,Response
from rating.serializer import android
# import datetime
class rating_view(APIView):
    def get(self,request):
        ob=Rating.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Rating()
        ob.u_id=request.data['u']
        ob.r_id=request.data['r_id']
        ob.rating=request.data['rating']
        ob.save()
        return HttpResponse('ok')
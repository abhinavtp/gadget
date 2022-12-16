from django.shortcuts import render

# Create your views here.
from oder.models import Order



# def paymnt(request,idd):
#     ob=Order.objects.get(o_id=idd)
#     ob.quantity=request.POST.get('')
#
#     return render(request,'oder/total_payment.html')
def add(request,idd):
    if request.method=="POST":
        object=Order()
        object.quantity=request.POST.get('qty')
        object.amount=request.POST.get('amount')
    return render(request,'oder/total_payment.html')



from django.http import HttpResponse
from rest_framework.views import APIView,Response
from oder.serializer import android
import datetime
class oder_view(APIView):
    def get(self,request):
        ob=Order.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Order()
        ob.u_id=request.data['u_id']
        ob.p_id=request.data['p_id']

        ob.date=datetime.datetime.today()
        ob.o_id=request.data['o_id']
        ob.amount=request.data['amount']
        ob.quantity=request.data
        ob.status='pending'
        ob.save()
        return HttpResponse('')
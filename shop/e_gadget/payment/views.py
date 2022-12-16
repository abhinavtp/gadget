from django.shortcuts import render

# Create your views here.
from payment.models import Payment
def paymnt(request):
    obj=Payment.objects.all()
    context={
        'objval':obj
    }
    return render(request,'payment/view_payment.html',context)
def paymnt(request):
    obj=Payment.objects.all()
    context={
        'objval':obj
    }
    return render(request,'payment/view_payment.html',context)


from django.http import HttpResponse
from rest_framework.views import APIView,Response
from payment.serializer import android
import datetime
class payment_view(APIView):
    def get(self,request):
        ob=Payment.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob=Payment()
        ob.u_id=request.data['u_id']
        ob.p_id=request.data['p_id']
        ob.payment_id=request.data['payment_id']

        ob.date=datetime.datetime.today()
        ob.o_id=request.data['o_id']
        ob.amount=request.data['amount']
        ob.status='pending'
        ob.save()
        return HttpResponse('post')
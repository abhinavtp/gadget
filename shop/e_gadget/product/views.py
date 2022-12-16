from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.


from product.models import Product
def add(request):
    if request.method == "POST":
        obj=Product()
        obj.product=request.POST.get('product')
        obj.image=request.POST.get('image')
        obj.price=request.POST.get('price')
        obj.specifications=request.POST.get('specification')
        obj.save()
    return render(request,'product/add_product.html')

def view_product(request):
    obj=Product.objects.all()
    context={
        'details':obj
    }
    return render(request,'product/c_view_product.html',context)
def manage(request):
    obj=Product.objects.all()
    context={
        'details':obj
    }
    return render(request,'product/manage_product.html',context)
def edit(request,idd):
    obj=Product.objects.filter(p_id=idd)
    context = {
        'details': obj
    }

    return render(request,'product/edit_product.html',context)
def add(request):
    if request.method == "POST":
        obj=Product()
        obj.product=request.POST.get('product')

        obj.price=request.POST.get('price')
        obj.specifications=request.POST.get('specification')
        fil = request.FILES['im']
        ff= FileSystemStorage()
        filename = ff.save(fil.name,fil)
        obj.image = fil.name

        obj.save()
    return render(request,'product/add_product.html')
def delete(request,idd):
    obj=Product.objects.get(p_id=idd).delete()
    return manage(request)
def reject(request,idd):
    obj=Product.objects.get(p_id=idd)
    obj.status="reject"
    obj.save()
    return manage(request)
def purcherse_prodect(request):
    obj=Product.objects.all()
    context={
        'objval':obj
    }
    return render(request,'product/purcharse_product.html',context)
def oder(request,idd):
    obj=Product.objects.get(p_id=idd)
    context={
        'details':obj
    }
    return render(request,'product/purcharse_product.html',context)
def total_payment(request,idd):
    return render(request,'oder/')

# def purcherse_prodect(request):
#     obj=Product.objects.all()
#     context={
#         'details':obj
#     }
#     return render(request,'product/purcharse_product.html',context)img = request.FILES['resume']




from django.http import HttpResponse
from rest_framework.views import APIView,Response
from product.serializer import android
# import datetime
class product_view(APIView):
    def get(self,request):
        ob=Product.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
     if request.method =="POST":
        obj=Product()
        obj.p_id=request.data['p_id']
        obj.product=request.data['product']
        obj.image=request.data['image']
        obj.price=request.data['price']
        obj.specifications=request.data['specifications']
        obj.status='pending'
        obj.save()
        return HttpResponse('success')

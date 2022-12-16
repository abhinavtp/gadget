
from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.


def login(request):
    if request.method == "POST":
        un = request.POST.get("usrname")
        ps = request.POST.get("password")
        print(ps)
        if Login.objects.filter(username=un, password=ps):
            obj = Login.objects.filter(username=un, password=ps)
            tp = ""
            for l in obj:
                tp = l.type
                uid = l.u_id
                if tp == "admin":
                    request.session["uid"] = uid
                    return render(request,'temp/adminhome.html')
                    # return HttpResponseRedirect('/temp/admin/')
                elif tp == "shop":
                    request.session["uid"] = uid
                    # return HttpResponseRedirect('/temp/staff/')
                    return render(request,'temp/shop_home.html')
                # elif tp == "custemer":
                #     request.session["uid"] = uid
                #     # return HttpResponseRedirect('/temp/student/')
                #     return render(request,'temp/custemer_home.html')
                elif tp == "service_engineer":
                    request.session["uid"] = uid
                    # return HttpResponseRedirect('/temp/staff/')
                    return render(request, 'temp/service_eng_home.html')
                else:
                    obje = "Incorrect username or password!!!"
                    context = {
                        'inv': obje,
                    }
                    return render(request, 'login/login.html', context)
        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'login/login.html', context)
    return render(request,'login/login.html')






# def add(request):
#     np=request.session["uid"]
#     ob = Login.objects.filter(type='custemer',user_id=np)
#     context = {
#         'objj': ob,
#     }
#     if request.method == "POST":
#         uname = request.POST.get("un")
#         passw = request.POST.get("pw")
#         new = request.POST.get("new")
#         if Login.objects.filter(type='custemer',username=uname, password=passw).exists():
#             obb = Login.objects.filter(type='custemer',username=uname, password=passw)
#             for obj in obb:
#                 obj.password=new
#                 obj.save()
#         else:
#             objlist = "Incorrect password... Please try again...!"
#             context2 = {
#                 'msg': objlist,
#             }
#             return render(request, "temp/custemer_home.html",context2)
#
#     return render(request, "temp/special.html", context)
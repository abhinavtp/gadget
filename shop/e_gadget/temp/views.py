from django.shortcuts import render

# Create your views here.

def tem(reruest):
    return render(reruest,'temp/special.html')



def adminhome(reruest):
    return render(reruest,'temp/adminhome.html')



def c_home(reruest):
    return render(reruest, 'temp/custemer_home.html')



def service_eng_home(reruest):
    return render(reruest,'temp/service_eng_home.html')



def shop_home(reruest):
    return render(reruest, 'temp/shop_home.html')
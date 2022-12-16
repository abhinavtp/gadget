from django.conf.urls import url
from temp import views
urlpatterns = [
   url(r'^mainhome/',views.tem),
   url(r'^adminhome/',views.adminhome),
   url(r'^shop_home/',views.shop_home),
   url(r'^c_home/',views.c_home),
   url(r'^service_eng_home/',views.service_eng_home),
]
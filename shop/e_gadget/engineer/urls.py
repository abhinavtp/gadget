from django.conf.urls import  url
from engineer import views
urlpatterns = [
url(r'^e_register',views.register),
]
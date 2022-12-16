from django.conf.urls import url
from customer import views

urlpatterns =[
    url(r'^register/',views.register),
    url(r'^manage/',views.manage),
    url(r'^approve/(?P<idd>\w+)',views.approve,name='apprv'),
    url(r'^reject/(?P<idd>\w+)', views.reject,name='rejct'),
    url(r'^android/',views.customer_view.as_view()),

]

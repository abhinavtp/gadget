from django.conf.urls import url
from service import views
urlpatterns =[
    url(r'^add/',views.add),
    url(r'^view',views.view_service),
    url(r'^manage/',views.manage),
    url(r'^approve/(?P<idd>\w+)',views.approve,name='approve'),
    url(r'^reject/(?P<idd>\w+)', views.reject,name='reject'),
    url(r'^request/(?P<idd>\w+)',views.rqst,name='service_request'),
    url(r'^request_view/', views.r_view),
    url(r'^/update/(?P<abc>\w+)', views.add_updte, name='update'),
    url(r'^android/',views.service_view.as_view()),

]
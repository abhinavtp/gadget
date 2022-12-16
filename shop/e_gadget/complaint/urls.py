from django.conf.urls import url
from complaint import views
urlpatterns =[
 url(r'^add_comp/',views.add),
 url(r'^view_comp/',views.view),
 url(r'^post_reply/(?P<abc>\w+)',views.post_reply,name='post_reply'),
 url(r'^view_rply',views.view_reply),
 url(r'^manage/',views.manage),
 url('android/',views.complaint_view.as_view())
 # url(r'^approve/(?P<abc>\w+)', views.approve, name='approv'),
 # url(r'^reject/(?P<abc>\w+)', views.reject, name='rejct'),
]
from django.conf.urls import url
from oder import views
urlpatterns = [
    url(r'^pur/(?P<idd>\w+)',views.add,name='pur'),
    url(r'^android/',views.oder_view.as_view()),

]
from django.conf.urls import url
from rating import views
urlpatterns =[
 url(r'^add/',views.add),
 url(r'^view/',views.view),
 url(r'^android',views.rating_view.as_view())
]
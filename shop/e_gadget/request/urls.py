from django.conf.urls import url
from request import views
urlpatterns =[
    url(r'^view_request/', views.request),
    url(r'^android/',views.request_view.as_view()),
    ]
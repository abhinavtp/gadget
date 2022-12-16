from django.conf.urls import url
from payment import views
urlpatterns = [
 url(r'^view_payment/',views.paymnt),
 url(r'^view_payment/', views.paymnt),
 url(r'^android',views.payment_view.as_view())

]
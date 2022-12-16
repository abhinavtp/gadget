from django.conf.urls import url
from product import views
urlpatterns = [
  url(r'^add_product',views.add),
  url(r'^c_view_product/',views.view_product),
  url(r'^manage/',views.manage),
  url(r'^edit/(?P<idd>\w+)',views.edit,name='edit'),
  url(r'^delete/(?P<idd>\w+)', views.delete,name='delete'),
  url(r'^pur_prd/',views.purcherse_prodect),
  url(r'^order/(?P<idd>\w+)',views.oder,name='order'),
  url(r'^view_product/',views.view_product),
  url(r'^android/',views.product_view.as_view()),

]
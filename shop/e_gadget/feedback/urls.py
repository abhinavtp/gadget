from django.conf.urls import url
from feedback import views
urlpatterns = [
  url(r'^add_feedback/',views.add),
  url(r'^view_feedback',views.view),
  url(r'^android/',views.feedback_view.as_view())
]
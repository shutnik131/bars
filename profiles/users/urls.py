from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'notes/$', views.notes)
)
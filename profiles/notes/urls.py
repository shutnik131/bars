from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.register),
    url(r'notes/$', views.notes),
)
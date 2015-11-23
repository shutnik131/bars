from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.register),
    url(r'^login/$', views.login, name='login'),
    url(r'add_note/$', views.add_notes),
    url(r'^notes/', views.notes),
)
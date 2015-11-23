from django.conf.urls import url
from . import views


urlpatterns = (
    url(r'^$', views.home_view, name='home'),
    url(r'^$', views.index_view, name='index'),
    url(r'^addnote/', views.add_note, name='addnote'),
)
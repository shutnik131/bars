"""bars_test_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from notes import views

urlpatterns = [
    url(r'^addnote/', views.add_note, name='addnote'),
    url(r'^$', views.index_view, name='index'),
    url(r'^$', views.home_view, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('notes.urls', namespace='notes')),
]

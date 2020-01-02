"""stemcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from schedules import views

app_name = "schedules"

urlpatterns = [
    url(r'', admin.site.urls),
    url(r'^kuliah/', views.Kuliah, name='kuliah'),
    url(r'^uploadsap/', views.uploadsap, name='uploadsap'),
    url(r'^calendar/$',views.CalendarView.as_view(),name='calendar'),
    url(r'^calendarnew/$',views.CalendarNewView.as_view(),name='calendarnew'),
    url(r'^stemkuliah/$',views.StemView.as_view(),name='stemkuliah'),
    url(r'^create/', views.JadwalCreate.as_view(), name='jadwalcreate'),
    url(r'^api/',include('schedules.urls')),
    url(r'^jadwalkuliah/', views.JadwalKuliah, name='jadwalkuliah'),
    url(r'^newuploadsap/', views.newuploadsap, name='newuploadsap'),
    url(r'^newkuliah/', views.NewKuliah, name='newkuliah')

]

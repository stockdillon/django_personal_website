from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    path('personal/', views.index, include('personal.urls')),
]

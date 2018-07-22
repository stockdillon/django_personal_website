from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib import admin
from object_detection.views import index

urlpatterns = [
    #url('^$', views.index, name='index'),
    path('', index.as_view(), name='index'),
]

from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib import admin
from object_detection.views import Index, Results

urlpatterns = [
    #url('^$', views.index, name='index'),
    path('', Index.as_view(), name='index'),
    path('results/', Results.as_view(), name='results'),
]

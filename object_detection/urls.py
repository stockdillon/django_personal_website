from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    #url('^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

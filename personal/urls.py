from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib import admin
from personal.views import index

urlpatterns = [
    #path('', views.index, name='index'),
    path('', index.as_view()),
    path('downloads/', views.downloads),
    path('downloads/resume.pdf/', views.download_resume),
    path('contact/', views.contact),
    path('blog/', views.blog),
]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from photo_gallery.views import Index, PhotosView

urlpatterns = [
    path('', Index.as_view()),
    path('sports/', views.sports),
    path('family/', views.family),    
]

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class index(TemplateView):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")
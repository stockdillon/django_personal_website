from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "mysite/home.html"
    def get(self, request):
        return render(request, self.template_name)

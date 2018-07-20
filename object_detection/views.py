from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from object_detection.forms import ImageUploadForm

from django.views.generic import TemplateView


# Create your views here.
class index(TemplateView):
    template_name = "object_detection/home.html"
    def get(self, request):
        #return HttpResponse("<h2>Please upload an image!</h2>")
        form = ImageUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("success")
        form = ImageUploadForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
        args = {'form': form, 'text': text}
        return render(request, self.template_name, context=args)

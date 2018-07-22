from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from .forms import ImageUploadForm, ResultModelForm
from .models import Result

from django.views.generic import TemplateView


# Create your views here.
class index(TemplateView):
    template_name = "object_detection/home.html"
    result_template = "object_detection/result.html"
    def get(self, request):
        #return HttpResponse("<h2>Please upload an image!</h2>")
        form = ImageUploadForm()
        return render(request=request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        form = ResultModelForm(request.POST,request.FILES,)
        if form.is_valid():
            text = "Successful upload."
            form.save()
        else:
            text = f"Upload failed. \n Errors: {form.errors} \n request.FILES: {request.FILES}"
        results = Result.objects.all()
        args = {"results": results, 'text': text,}
        return render(request=request, template_name=self.result_template, context=args)


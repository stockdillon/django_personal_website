from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from .forms import ImageUploadForm, ResultModelForm
from .models import Result
import requests
import boto3
import cv2 as cv
from uuid import uuid4

from django.views.generic import TemplateView
from django.shortcuts import redirect


# Create your views here.
class index(TemplateView):
    template_name = "object_detection/home.html"
    result_template = "object_detection/results.html"
    def get(self, request):
        #return HttpResponse("<h2>Please upload an image!</h2>")
        form = ImageUploadForm()
        return render(request=request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        #unique_id = uuid4().urn.split(":")[2]
        #s3 = boto3.client('s3')
        #s3.upload_file("originals", Key=unique_id)
        lambda_response=requests.get(
            url="https://g7l8fkmf3f.execute-api.us-east-1.amazonaws.com/default/DjangoFacialRecognition",
            )        
        # Above this comment is temporary code       
        form = ResultModelForm(request.POST,request.FILES,)
        if form.is_valid():
            text = f"Successful upload. <br> Response from AWS Lambda: {lambda_response}"
            instance = form.save()
            instance.process()
        else:
            text = f"Upload failed. \n Errors: {form.errors} \n request.FILES: {request.FILES}"        
        return redirect("results/", permanent=True)


class results(TemplateView):
    template_name = "object_detection/results.html"

    def get(self, request):
        results = Result.objects.all()
        #for result in results:
        #    result.process()
        text = ""
        args = {"results": results, 'text': text,}
        #return render(request=request, template_name=self.result_template, context=args)
        return render(request=request, template_name=self.template_name, context=args)        
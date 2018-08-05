from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from django.views.generic import TemplateView

#def index(request):
#    return render(request, 'personal/home.html')

def downloads(request):
    return render(request, 'personal/downloads.html')

def contact(request):
    return render(request, 'personal/contact.html')

def blog(request):
    return render(request, 'personal/blog.html')

def download_resume(request):
    filename = 'Dillon_Stock_Resume_2018.pdf'
    content = FileWrapper(filename)
    response = HttpResponse(content, content_type='application/pdf')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % 'Dillon_Stock_Resume_2018.pdf'
    return response

class Index(TemplateView):
    template_name = "personal/home.html"
    def get(self, request):
        return render(request, self.template_name)
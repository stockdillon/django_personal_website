from django.shortcuts import render
from django.views.generic import TemplateView
import os

# Create your views here.
class Index(TemplateView):
    template_name = "photo_gallery/index.html"
    def get(self, request):
        return render(request, self.template_name)

class PhotosView(TemplateView):
    template_name = "photo_gallery/photos.html"
    def get(self, request):
        return render(request, self.template_name)

class SportsPhotosView(PhotosView):
    def get(self, request):
        return render(request, self.template_name)

def sports(request):
    print(os.getcwd())
    img_filenames = os.listdir('photo_gallery/static/photo_gallery/img/sports')
    img_paths = ['photo_gallery/img/sports/' + filename for filename in img_filenames]
    print(img_paths)
    args= dict(img_paths=img_paths)
    return render(request, 'photo_gallery/photos.html', context=args)

def family(request):
    img_filenames = os.listdir('photo_gallery/static/photo_gallery/img/family')
    img_paths = ['photo_gallery/img/family/' + filename for filename in img_filenames]
    args= dict(img_paths=img_paths)
    return render(request, 'photo_gallery/photos.html', context=args)

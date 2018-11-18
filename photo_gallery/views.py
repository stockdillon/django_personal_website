from django.shortcuts import render
from django.views.generic import TemplateView
import os

IMAGE_DISPLAY_ROW_LENGTH = 3

# Create your views here.
class Index(TemplateView):
    template_name = "photo_gallery/index.html"
    def get(self, request):
        return render(request, self.template_name)

def chunk(img_paths, row_length):
    """
    splits the image paths into lists (rows) of length 3 to display in our template
    """
    return [img_paths[i:i+row_length] for i in range(0,len(img_paths)-len(img_paths)%row_length,row_length)]

def render_photos(request, category):
    img_filenames = os.listdir(f'photo_gallery/static/photo_gallery/img/{category}')
    img_paths = [f'photo_gallery/img/{category}/{filename}' for filename in img_filenames]
    #print(img_paths)
    img_rows = chunk(img_paths, row_length=IMAGE_DISPLAY_ROW_LENGTH)
    args= dict(img_rows=img_rows)
    #print(f"Args: {args}")
    return render(request, 'photo_gallery/photos.html', context=args)

def sports(request):
    #category = request.path_info.split('/')[2]
    category = "sports"
    return render_photos(request, category)

def family(request):
    category = "family"
    return render_photos(request, category)  

class PhotosView(TemplateView):
    category = ""
    template_name = "photo_gallery/photos.html"
    def get(self, request, category):
        return render_photos(request, category)
        #return render(request, self.template_name)

class SportsPhotosView(PhotosView):
    def get(self, request):
        return render(request, self.template_name)
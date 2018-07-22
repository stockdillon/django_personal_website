from django import forms
from .models import Result

class ImageUploadForm(forms.Form):
    description = forms.CharField()
    image = forms.FileField() 

class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('image',)
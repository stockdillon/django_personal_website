from django import forms
from .models import Result

class ImageUploadForm(forms.Form):
    description = forms.CharField(required=False, label='', help_text='Enter a description')
    #image = forms.FileField(widget=forms.ImageField(attrs={'class':'form-control', 'type':'image'}), label='') 
    image = forms.FileField(label='', help_text='') 

class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('image',)
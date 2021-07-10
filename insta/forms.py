from .models import Post
from django import forms

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','image_name','image_caption']
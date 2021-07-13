from . models import Post,Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','name','caption']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']
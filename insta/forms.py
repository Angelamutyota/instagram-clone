from . models import Comment, Post,Profile
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
        fields = ['profile', 'bio']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'post', 'user' ]

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

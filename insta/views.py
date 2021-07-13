from insta.forms import UploadImageForm, CreateUserForm
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Post, Profile, Comment, Follow
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def welcome(request):
    posts=Post.objects.all()
    return render(request, 'index.html',  {"posts":posts})

def comments(request,id):
    all_comments = Comment.get_comments(id)
    return render(request, 'comments.html', {"comments":all_comments})

def profile (request, uname):
    profile = Profile.objects.filetr(user = uname)

def upload_image(request):
    current_user = request.user
    if request.method == 'post':
        form = UploadImageForm(request.POST, request.files)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect()
    
    else:
        form = UploadImageForm()
    return render(request,'new_image.html', {"form": form})

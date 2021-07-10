from insta.forms import UploadImageForm
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Post, Profile, Comment, Follow


# Create your views here.
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
    return render(request,'index.html', {"form": form})

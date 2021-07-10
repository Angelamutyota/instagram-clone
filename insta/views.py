from django.shortcuts import render
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

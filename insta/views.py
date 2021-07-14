from insta.forms import UploadImageForm, CreateUserForm, UpdateProfileForm
from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Post, Profile, Comment, Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registerPage(request):
    form = CreateUserForm
    profile = Profile()
    profile.user = User
    profile.save()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
        name = form.cleaned_data.get("username")
        messages.success(request,name+"'s account successfully created")
    context = {'form':form, 'profile':profile}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Incorrect Username or Password')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')

def welcome(request):
    posts=Post.objects.all()
    return render(request, 'index.html',  {"posts":posts})

@login_required(login_url="login")
def comments(request):
    image_id= request.GET.get("comments_image_id")

    all_comments = Comment.get
    comments = []
    return render(request,"comments.html",{"all_comments":all_comments})

@login_required(login_url="login")
def profile(request):
    images = request.user.profile.images.all()
    if request.method == 'POST':
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {"images":images,"profile_form":profile_form})

@login_required(login_url="login")
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadImageForm(request.POST or None, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user.profile
            image.save()
        return redirect('index')
    
    else:
        form = UploadImageForm()
    return render(request,'new_image.html', {"form": form})

@login_required(login_url="login")
def search_profile(request):
    if 'username' in request.GET and request.GET["username"]:
        search_name = request.GET.get("username")
        searched_profiles = Profile.search_profile(search_name)
        message = f"{search_name}"

        return render(request,"search.html",{"message":message,"searched_profiles":searched_profiles})
    else:
        message = "Enter a username to search"
        return render(request,"search.html",{"message":message})

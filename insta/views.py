from insta.forms import UploadImageForm, CreateUserForm, UpdateProfileForm, NewCommentForm, UpdateUserForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http  import HttpResponse, HttpResponseRedirect
from .models import Post, Profile, Comment, Follow
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    
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

@login_required(login_url="login")
def welcome(request):
    posts=Post.objects.all()
    user = User.objects.all()
    return render(request, 'index.html',  {"posts":posts,"user":user })

@login_required(login_url="login")
def comments(request,id):
    all_comments = Comment.get_comments(id)
    image = get_object_or_404(Post, pk=id)
    
    form = NewCommentForm()
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.author = request.user
            comment.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = NewCommentForm()
    return render(request,"comments.html",{"all_comments":all_comments,"form":form})       

@login_required(login_url='login')
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    images = request.user.profile.images.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'prof_form': prof_form,
        'images': images,
        'user_form': user_form,
    }
    return render(request, 'profile.html', context)

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

@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('user_profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    followers = Follow.objects.filter(followers=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.following:

            follow_status = True
        else:
            follow_status = False
    context = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    return render(request, 'user_profile.html', context)

def follow(request, pk):
    if request.method == 'GET':
        user = Profile.objects.get(pk=pk)
        follow = Follow(following=request.user.profile, followers=user)
        follow.save()
        
    return redirect('user_profile', user.user.username)

def unfollow(request, pk):
    if request.method == 'GET':
        user_ = Profile.objects.get(pk=pk)
        unfollow= Follow.objects.filter(following=request.user.profile, followers=user_)
        unfollow.delete()
        return redirect('user_profile', user_.user.username) 
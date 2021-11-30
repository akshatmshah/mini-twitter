from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Tweet, Profile
from django.views import generic
from main.forms import TweetForm
from taggit.models import Tag
from django.http import HttpResponseRedirect

def splash(request):
    return render(request, "home.html", {})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/feed")
    return render(request, 'login.html', {})

def signup_(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
        login(request, user)
        return redirect('/feed')
    elif request.method == "GET":
        return render(request, 'signup.html', {})

class Feed(generic.ListView):
    template_name = 'feed.html'
    context_object_name = 'tweets'
    def get_queryset(self):
        return Tweet.objects.filter(time__lte=timezone.now()).order_by('-time')

def LikeView(request, post_id):
    post = get_object_or_404(Tweet, pk=post_id)
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    next = request.POST.get('next', '/')
    return redirect(next)


def create_post(request):
    form = TweetForm
    if request.method == 'POST': 
        postf = TweetForm(request.POST)
        if postf.is_valid():
            profile = postf.save(commit=False)
            profile.user = request.user
            text = request.POST.dict()['description'].split()
            profile.save()
            for tag in text:
                if tag.startswith("#"):
                    newTag = tag.strip("#")
                    profile.tags.add(newTag)
            postf.save_m2m()
            return redirect('/feed')
    return render(request, 'post.html', {'form': form})
    
def get_user_profile(request, username):
    user = get_object_or_404(User, username=username)
    prof = Profile.objects.get_or_create(user=user)
    tweet = Tweet.objects.filter(user = user)
    return render(request, "profile.html", {"profile": prof[0], "tweets": tweet})

def get_hashtag(request, hashtag):
    tweet = Tweet.objects.filter(tags__name__in=[hashtag])
    return render(request, "profile.html", {"profile": hashtag,"tweets": tweet})

def delete_post(request, post_id):
    post = get_object_or_404(Tweet, pk=post_id, user=request.user)
    post.delete()
    return redirect("/feed")

def logout_(request):
    logout(request)
    return redirect("/")    
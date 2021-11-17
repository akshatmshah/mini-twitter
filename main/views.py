from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

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

def feed(request):
    return render(request, "feed.html", {})


def logout_(request):
    logout(request)
    return redirect("/")    
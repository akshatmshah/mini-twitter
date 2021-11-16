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
            return redirect("/")
    return render(request, 'login.html', {})

def signup(request):
	user = User.objects.create_user(username=request.POST['username'],
					email=request.POST['email'],
					password=request.POST['password'])
	login(request, user)
	return redirect('/')


def logout_(request):
    logout(request)
    return redirect("login")    
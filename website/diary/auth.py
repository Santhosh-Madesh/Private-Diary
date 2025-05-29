from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,"Username already taken!")
                return redirect("signup")
            else:
                user = User(username=username)
                user.set_password(password)
                user.save()
                return redirect("login")
    form = SignupForm()
    return render(request,"diary/signup.html",{"form":form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request,username=username,password=password)

            if user is None:
                messages.error(request,"Invalid credentials")
                return redirect("login")
            else:
                login(request,user)
                return redirect("index")
    form = LoginForm()
    return render(request,"diary/login.html",{"form":form})
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
                messages.success(request,"Successfully Logged In!")
                return redirect("index")
    form = LoginForm()
    return render(request,"diary/login.html",{"form":form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            old_password = form.cleaned_data["current_password"]
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_new_password"]
            user = request.user
            if user.is_authenticated:
                current_username = user.username
                if username == current_username:
                    correct_user = authenticate(request,username=username,password=old_password)
                    if correct_user is None:
                        messages.error(request,"Invalid password, please enter a valid password")
                        return redirect("change_password")
                    else:
                        if new_password==confirm_password:
                            user = User.objects.get(username=username)
                            user.set_password(new_password)
                            user.save()
                            return redirect("login")
                        else:
                            messages.error(request,"new password and confirm password do not match") 
                            return redirect("change_password")
                else:
                    messages.error(request,"Invalid Username")
                    return redirect("change_password")
            else:
                messages.error(request,"Please log in to your account")
                return redirect("login")
    form = ChangePasswordForm()
    return render(request,"diary/change_password.html",{"form":form})

def logout_page(request):
    logout(request)
    messages.success(request,"Logged out Successfully!")
    return redirect("login")
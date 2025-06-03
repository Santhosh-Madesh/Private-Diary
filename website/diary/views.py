from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm, DashboardForm, DashboardUpdateForm, ProfileModelForm
from .models import DiaryModel, Profile
from django.contrib.auth.models import User

@login_required
def index(request):
    dm = DiaryModel.objects.all()
    if dm:
        context = []
        for field in dm:
            context.append(
                {
                    "date":field.date,

                    "content":field.content,
                    }
                    )
        return render(request,"diary/index.html",{"context":context})
    messages.error(request,"No data available!")
    return render(request,"diary/index.html")

@login_required
def write_diary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            content = form.cleaned_data["content"]
            dm = DiaryModel(data=date,content=content)
            dm.save()
            return redirect("index")
    form = DiaryForm()
    return render(request,"diary/write_diary.html",{"form":form})



def personal_dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ProfileModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("dashboard")
        profile = Profile.objects.filter(user=request.user)
        if profile:
            user = User.objects.filter(username=request.user.username)
            return render(request,"diary/dashboard.html",context={"profile":profile,"user":user})
        else:
            form = ProfileModelForm()
            return render(request,"diary/dashboard_form.html",{"form":form})
    else:
        messages.error(request,"Please log in to access personal dashboard")
        return redirect("login")

@login_required
def update_dashboard(request):
    if request.method == "POST":
        form = ProfileModelForm(request.POST, request.FILES)
        if form.is_valid():
            age = form.cleaned_data["age"]
            bio = form.cleaned_data["bio"]
            instagram_id = form.cleaned_data["instagram_id"]

            profile = Profile.objects.get(user=request.user)
            profile.age = age
            profile.bio = bio
            profile.pfp = request.FILES["pfp"]
            profile.save()
            

            messages.success(request,"Dashboard Successfully Updated!")
            return redirect("dashboard")

    profile = Profile.objects.get(user=request.user)
    age = profile.age
    bio = profile.bio
    instagram_id = profile.instagram_id
    pfp = profile.pfp

    form = ProfileModelForm(initial={'age':age,'instagram_id':instagram_id,'bio':bio})
    return render(request,"diary/dashboard_update.html",{"form":form})
from django.shortcuts import render
from .forms import DiaryForm

def index(request):
    return render(request,"diary/index.html")

def write_diary(request):
    form = DiaryForm()
    return render(request,"diary/write_diary.html",{"form":form})
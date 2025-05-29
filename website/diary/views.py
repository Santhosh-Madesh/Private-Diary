from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DiaryForm
from .models import DiaryModel

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
    messages.error(request,"No data is available!")
    return render(request,"diary/index.html")

def write_diary(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            content = form.cleaned_data["content"]
            dm = DiaryModel(date=date,content=content)
            dm.save()
            return redirect("index")
    form = DiaryForm()
    return render(request,"diary/write_diary.html",{"form":form})
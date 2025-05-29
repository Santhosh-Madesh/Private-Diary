from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DiaryForm
from .models import DiaryModel

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
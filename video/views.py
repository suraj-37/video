from calendar import HTMLCalendar
import calendar
from cgitb import small, text
from posixpath import split
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Video_form
from .models import Video
from datetime import datetime

def upload_video(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            video= form.cleaned_data['video']

            # price of video output in terminal 

            filesize=video.size
            if filesize<4194304000:
                print("5$")
            else:
                print("12.5$") 
                 
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=Video_form()  
    return render(request,'upload_video.html',{"form":form})          

def videos(request):
    all_video=Video.objects.all()
    return render(request,'videos.html',{"all":all_video})


def videos_sort_by_date(request): 
        video_list_by_time=''
        if request.method=="POST":
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            biggestsize=request.POST.get('biggest size')
            video_list_by_time=Video.objects.filter(created_time__gte=fromdate,created_time__lte=todate)
        return render (request,'videos_search.html',{"all":video_list_by_time})
 


        
    
from django.shortcuts import render
from pytube import *

# Create your views here.


def youtube(request):
    if request.method=='POST':
        url=request.POST['link']
        video=YouTube(url)
        stream=video.streams.get_lowest_resolution()
        print(stream)
        stream.download()
        return render(request,'index.html')
    return render(request,'index.html')

from django.shortcuts import render,redirect
from .models import Video,Shorts
from .forms import VideoUploadForm,ShortsForm
from django.contrib import messages

def home(request):
    return render(request,'home.html')
def upload(request):

    if request.method=='POST':
        form=VideoUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'video uploaded successfully!')
            return redirect('upload')
    else:
        form = VideoUploadForm()
        short=ShortsForm()
        return render(request,'upload.html',{'form':form,'shorts':short})
def uploadshorts(request):
    if request.method=='POST':
        form=ShortsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'shorts uploaded successfully!')
            return redirect('upload')

    else:
        form = VideoUploadForm()
        short=ShortsForm()
        return render(request,'upload.html',{'form':form,'shorts':short})

def videolist(request):
        videos=Video.objects.all()
        return render(request,'videolist.html',{'video':videos})

def delete(request,id):
    obj=Video.objects.get(id=id)
    obj.delete()
    return redirect("video")

def deleteshort(request,id):
    obj=Shorts.objects.get(id=id)
    obj.delete()
    return redirect("shorts")

def search(request):
    if request.method=='POST':
        video=request.POST.get('q')
        short=request.POST.get('q')
        if video:
            video=Video.objects.filter(title__icontains=video)
            shorts=Shorts.objects.filter(title__icontains=short)
            return render(request,'searchshow.html',{'video':video,'short':shorts})
        else:
            return redirect('/')
            messages.warning(request, 'no videos found')

def shorts(request):
    shorts=Shorts.objects.all()
    return render(request,'shorts.html',{'short':shorts})

def exit(request):
    return render(request,'exit.html')

def help(request):
    return render(request,'help.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def feedback(request):
    return render(request,'feedback.html')
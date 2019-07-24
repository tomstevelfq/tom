#coding:utf-8
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse,HttpResponseRedirect
import datetime

# Create your views here.

def vue(request):
    return render(request,'hello.html',locals())

def index(request):
    return render(request,'index.html',locals())

def detail(request,question_id):
    return HttpResponse("you're looking at question %s"%question_id)

def results(request,question_id):
    response="you're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s" % question_id)

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def upload_file(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')

    else:
        form=UploadFileForm()
    return render(request,'upload.html',{'form':form})

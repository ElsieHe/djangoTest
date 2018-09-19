# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sign.models import Event, Guest
# Create your views here.


def index(request):
#    return HttpResponse("Hello Diango!")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username, password = password)
        #if username == 'admin' and password == 'admin123':
        if user is not None:
            auth.login(request, user) #登陆
            #response.set_cookie('user',username, 3600)
            request.session['user'] = username
            response =  HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request, "event_manage.html",{"user":username, "events":event_list})
    #username = request.COOKIES.get('user','')#读取浏览器cookie
    #username = request.session.get('user','')#读取浏览器session
    #return render(request, "event_manage.html", {"user":username})

@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html",{"user":username, "events":event_list})

@login_required
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        #如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html",{"user":username,"guests":contacts})

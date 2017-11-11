# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import request
from django.shortcuts import render,redirect
from OL_admin.models import *
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def login(request):
    return render(request,'OL_admin/login.html')

def loginhandle(request):
    username =  request.POST.get('username').encode('utf-8')
    pwd = request.POST.get('pwd').encode('utf-8')
    userInfo = User.objects.filter(username=username)
    if userInfo:
        if userInfo[0].pwd == pwd:
            response = HttpResponseRedirect('/lesson/admin/index')
            response.set_cookie('username',username)
            return response
    return redirect('/lesson/admin/login')

def index(request):
    loginusername = request.COOKIES['username']
    content = {
        'loginusername':loginusername
    }
    return render(request,'OL_admin/index.html',content)

def welcome(request):
    return render(request,'OL_admin/welcome.html')


def article_list(request):
    return render(request,'OL_admin/article-list.html')

def admin_role(request):
    return render(request,'OL_admin/admin-role.html')

def admin_permission(request):
    return render(request,'OL_admin/admin-permission.html')

def admin_list(request):
    return render(request,'OL_admin/admin-list.html')

#角色添加
def admin_add(request):
    return render(request,'OL_admin/admin-add.html')

#管理员添加
def admin_role_add(request):
    return render(request,'OL_admin/admin-role-add.html')
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator,Page
from OL_teacher.models import *
# Create your views here.


# 题目
def topic(request):
    a = request.POST.get('A')
    b = request.POST.get('B')
    c = request.POST.get('C')
    d = request.POST.get('D')
    tureAnswer =  request.POST.get('answer')
    examtopic =  request.POST.get('topic')
    typeof = request.POST.get('test3')
    level = request.POST.get('test2')
    point = request.POST.get('point')
    allSelect = []
    allSelect.append(a)
    allSelect.append(b)
    allSelect.append(c)
    allSelect.append(d)
    topic = Exam()
    topic.eTopic = examtopic
    topic.eAllSelect = allSelect
    topic.eTrueSelect = tureAnswer
    topic.eLevel = level
    topic.eType = typeof
    topic.ePoint = point
    topic.save()
    return redirect('/teacher/add_exam/')




from django.shortcuts import render,redirect
from .models import UserInfo
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
# Create your views here.

def User_Register(request):
    context = {
        'title': '用户注册',
    }
    return render(request,'OL_user/register.html',context)


def User_Register_handler(request):
    UserName = request.POST.get('username')
    UserPwd = request.POST.get('username_pwd')
    UserPwdA = request.POST.get('username_pwd')
    UserEmail = request.POST.get('username_email')
    RememberLogin= request.POST.get('Remember')
    context = {
    }
    return render(request,'OL_user/register.html',context)




def User_login(request):
    UserName = request.COOKIES.get('username','')
    context = {
        'title': '用户注册',
        'LOGIN_state': 1,
    }
    return render(request,'OL_user/login.html',context)

def User_login_handler(request):
    UserName = request.POST.get('username')
    UserPwd = request.POST.get('username_pwd')
    RememberLogin= request.POST.get('Remember')
    if "@" in UserName:
        Old_users = UserInfo.objects.filter(User_email=UserName)
    else:
        Old_users = UserInfo.objects.filter(User_name=UserName)
    if len(Old_users)==1:
        encipherment = sha1()
        encipherment.update(UserPwd.encode('utf-8'))
        UserPwd_encipherment = encipherment.hexdigest()
        if UserPwd_encipherment == Old_users[0].User_pwd:
            url = request.COOKIES.get('url','/')
            cookiesWarn = HttpResponseRedirect(url)
            cookiesWarn.set_cookie('url','',max_age=-1)
            if RememberLogin != 'on' :
                cookiesWarn.set_cookie('username',UserName)
            else:
                cookiesWarn.set_cookie('username','',max_age=-1)
            request.session['user_id']=Old_users[0].id
            request.session['user_name']=UserName
            return cookiesWarn
        else:
            context = {
                'title': '用户注册',
                'LOGIN_state': 2,
                'username': UserName,
            }
            return render(request,'OL_user/mycourse.html',context)
    else:
        context = {
            'title': '用户注册',
            'LOGIN_state': 1,
        }
        return render(request, 'OL_user/login.html', context)
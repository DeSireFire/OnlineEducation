from django.shortcuts import render,redirect
from OL_user.models import UserInfo
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
import re
# Create your views here.

def User_Register(request):
    context = {
        'title': '用户注册',
        'LOGIN_state': 1,
        'Warn': '',
    }
    return render(request,'OL_user/register.html',context)


def User_Register_handler(request):
    UserEmail = request.POST.get('username_email')
    UserName = request.POST.get('username')
    UserPwd = request.POST.get('username_pwd')
    UserPwdA = request.POST.get('username_pwdA')
    Old_users_User_email = UserInfo.objects.filter(User_email=UserName)
    Old_users_User_name = UserInfo.objects.filter(User_name=UserName)
    print(UserEmail)
    print(UserName)
    print(UserPwd)
    print(UserPwdA)
    print(re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',UserEmail))
    if UserEmail and UserName and UserPwd and UserPwdA != '':
        if UserPwd != UserPwdA:
            context = {
                'title': '用户注册',
                'LOGIN_state': 1,
                'Warn': '两次密码输入不一致！',
            }
            return render(request, 'OL_user/register.html', context)
        elif re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',UserEmail) == None:
            context = {
                'title': '用户注册',
                'LOGIN_state': 1,
                'Warn': '请输入正确的电子邮箱！',
            }
            return render(request, 'OL_user/register.html', context)
        elif len(Old_users_User_email) or len(Old_users_User_name) ==1:
            #判断注册用户名和邮箱是否已存在
            context = {
                'title': '用户注册',
                'LOGIN_state': 1,
                'Warn': '该昵称或邮箱已存在！',
            }
            return render(request, 'OL_user/register.html', context)
        else:
            print('注册信息验证OK！')
            encipherment = sha1()
            encipherment.update(UserPwd.encode('utf-8'))
            UserPwd_encipherment = encipherment.hexdigest()
            print(UserPwd_encipherment)
            print('加密处理完成!')
            NewUser = UserInfo()
            NewUser.User_email = UserEmail
            NewUser.User_name = UserName
            NewUser.User_pwd = UserPwd_encipherment
            NewUser.User_pwd = UserPwd_encipherment

            NewUser.save()
            print('用户信息保存入库！')
            context = {
                'title': '用户注册',
                'LOGIN_state': 2,
                'Warn': '注册成功！',
                'username': UserName,
            }
            return render(request, 'OL_user/login.html', context)


    else:
        context = {
            'title': '用户注册',
            'LOGIN_state': 1,
            'Warn': '用户注册信息未填写完整！',

        }
        return render(request, 'OL_user/register.html', context)




def User_login(request):
    UserName = request.COOKIES.get('username','')
    context = {
        'title': '用户登录',
        'Warn': '',
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
    print(Old_users)
    print(type(Old_users))


    if len(Old_users)==1:
        # 查找用户名是否存在
        encipherment = sha1()
        encipherment.update(UserPwd.encode('utf-8'))
        UserPwd_encipherment = encipherment.hexdigest()
        print('UserPwd_encipherment:%s'%UserPwd_encipherment)
        print('Old_users:%s'%Old_users[0].User_pwd)


        if UserPwd_encipherment == Old_users[0].User_pwd:
            # 验证密码是否与数据库一致
            url = request.COOKIES.get('url','/')
            #跳转操作
            cookiesWarn = HttpResponseRedirect(url)
            #用HttpResponseRedirect实现重定向传参
            cookiesWarn.set_cookie('url','',max_age=-1)
            if RememberLogin != 'on' :
                # 是否选择记住我！
                cookiesWarn.set_cookie('username',UserName)
            else:
                cookiesWarn.set_cookie('username','',max_age=-1)
            request.session['user_id']=Old_users[0].id
            request.session['user_name']=UserName

            context = {
                'title': '用户登录',
                'Warn': '登录成功！',
                'LOGIN_state': 2,
                'username': UserName,
            }
            return cookiesWarn

        else:
            # 密码验证失败
            context = {
                'title': '用户登录',
                'Warn': '该用户名不存在！',
                'LOGIN_state': 1,
                'username': UserName,
            }
            return render(request,'OL_user/login.html',context)
    else:
        context = {
            'title': '用户登录',
            'Warn': '该用户名不存在！去注册一个吧～',
            'LOGIN_state': 1,
        }
        return render(request, 'OL_user/login.html', context)
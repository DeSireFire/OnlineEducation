# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 用户邮箱
    User_email = models.CharField(max_length=100,unique=True)
    # 用户昵称
    User_name=models.CharField(max_length=20,unique=True)
    # 用户密码
    User_pwd=models.CharField(max_length=40)
    # 用户权限
    User_permission=models.CharField(max_length=20,default='3')
    # 用户身份
    User_role=models.CharField(max_length=20)
    # 用户简介信息
    User_info=models.CharField(max_length=20,default='')
    # 用户地址
    User_address=models.CharField(max_length=100,default='')
    # 用户手机
    User_phone=models.CharField(max_length=11,default='')


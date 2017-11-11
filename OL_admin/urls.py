#coding:utf-8
from django.conf.urls import include, url
from OL_admin.views import *

urlpatterns = [
    url(r'^login$',login),
    url(r'^loginhandle$',loginhandle),
    url(r'^index$',index),
    url(r'^index/welcome$',welcome),
    url(r'^index/article-list$',article_list),
    url(r'^index/admin-role$',admin_role),
    url(r'^index/admin-permission$',admin_permission),
    url(r'^index/admin-list$',admin_list),
    url(r'^index/admin-add$',admin_add),
    url(r'^index/admin-role-add$',admin_role_add),
]

from django.conf.urls import url
from OL_user import views


urlpatterns=[
    url(r'^register/$',views.User_Register),
    url(r'^login/$', views.User_login),
    # url(r'^register_handle/$',views.register_handle),
    # url(r'^register_skip/$', views.register_skip),
    url(r'^login_handle/$', views.User_login_handler),
    # url(r'^logout/$',views.login_skip),
    # url(r'^info/$', views.info),
    # url(r'^site/$', views.site),
]
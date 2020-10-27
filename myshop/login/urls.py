from django.conf.urls import include,url
from login.views import *
from django.contrib.auth import views as auth_views

app_name="login"
urlpatterns = [
     url(r'^$',login,name='login'),
    url(r'^auth_view/$',auth_view,name="auth_view"),
    url(r'^logout/$',logout,name="logout"),
    url(r'^loggedin/$',loggedin),
    url(r'^invalid/$',invalid_login),
    url(r'^register/$',register_user,name='register'),
    url(r'^register_success/$',register_success,name="success")
   
    ]                  

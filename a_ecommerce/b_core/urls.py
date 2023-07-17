from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as login_views


# Memanggil Views Ke dalam Urls
from . import views

from .forms import LoginForm

app_name = 'b_core'

urlpatterns = [
    path('', views.index, name='index-page'),
    path('login/', login_views.LoginView.as_view(template_name='b_core/login.html',authentication_form=LoginForm),name='login-page'),
    path('sigup/', views.signup, name='signup-page'),
]
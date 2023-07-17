from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as login_views


# Memanggil Views Ke dalam Urls
from . import views

app_name = 'f_blog'

urlpatterns = [
    path('', views.Blog_atala, name='blog-page'),

    # Memanggil Blog Detail
    path('blog_datail/<int:pk>', views.Blog_detail, name='blog-detail'),
    path('comment/', views.Blog_coment, name='comment-page'),
]
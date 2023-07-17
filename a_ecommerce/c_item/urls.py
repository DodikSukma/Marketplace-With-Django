from django.contrib import admin
from django.urls import path


# Memanggil Views Ke dalam Urls
from . import views
app_name = 'c_item'

urlpatterns = [
    path('', views.items, name='items-page'),
    path('<int:pk>/', views.item_detail, name='ditail-item-page'),
]
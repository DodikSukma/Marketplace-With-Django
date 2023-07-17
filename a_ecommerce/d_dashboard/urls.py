from django.urls import path

from . import views

app_name = 'd_dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard-page'),
    path('add_product/', views.new_item_owner, name='add-item'),
    path('detail/<int:pk>/', views.item_detail_owner, name='ditail-item-page-owner'),
    path('delete/<int:pk>/', views.delete_item_owner, name='delete-item-page-owner'),
    path('update/<int:pk>/', views.edit_item_owner, name='edit-item-page-owner'),

    # Path Blog_admin
    path('blog_admin/', views.dashboard_blog_admin, name='blog-admin'),
    path('blog_admin/add_product/', views.add_blog, name='add-item-blog-admin'),
    path('blog_admin/detail/<int:pk>/', views.blog_detail, name='ditail-item-page-blog-admin'),
    path('blog_admin/delete/<int:pk>/', views.delete_blog, name='delete-item-page-blog-admin'),
    path('blog_admin/update/<int:pk>/', views.edit_blog, name='edit-item-page-blog-admin'),

]
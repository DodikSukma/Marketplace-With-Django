# Create your views here.
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
# Create your views here.


from django.db.models import Q

# Create your views here.
from django.http import HttpResponse


# Membuat Fungsi Blog
from .models import Category_blog, Blog,Comment
def Blog_atala(request):
    query = request.GET.get('query', '')


    category_id = request.GET.get('category',0)

    categories = Category_blog.objects.all()

    Blogs = Blog.objects.all()

    if category_id:
        Blogs = Blogs.filter(category=category_id)
    
    if query:
        Blogs = Blogs.filter(Q(content_1__icontains=query) | Q(title__icontains=query))


    context = {
        'categories': categories,
        'Blogs': Blogs,
        'query': query,
        'category_id': int(category_id),
    }
    return render(request, 'f_blog/f_blog_atala.html', context)

# Membuat Blog Detail
def Blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    comment = Comment.objects.all()
    # Membuat related Blog
    related_blog = Blog.objects.filter(category=blog.category).exclude(pk=pk)[0:3]
    context = {
        'blog': blog,
        'related_blog': related_blog,
    }
    return render(request, 'f_blog/f_blog_detail.html', context)

# Membuat Fungsi Comement Pada Blog
from .models import Comment
def Blog_coment(request):
    comment = Comment.objects.all()
    context = {
        'comment': comment,
        }
    return render(request, 'f_blog/coba.html', context)
    
from django.shortcuts import render, get_list_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.db.models import Q

# Create your views here.

from c_item.models import Item,Category

@login_required
def dashboard(request):

    query = request.GET.get('query', '')

    # creat a get category_id
    category_id = request.GET.get('category', 0)

    # creat a get all object Category with categories
    categories = Category.objects.all()

    # creat a get all object of Item 
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(descriptions__icontains=query))
    context = {
        'items': items,
        'categories': categories,
        'query': query,
        'category_id': int(category_id),
    }
    return render(request, 'd_dashboard/dashboard.html', context)

# Membuat Fungsi detail
@login_required
def item_detail_owner(request, pk):
    item = Item.objects.get(id=pk)

    context = {
        'items': item,
        }
    return render(request, 'd_dashboard/detail_owner.html', context)



# Membuat New Product
from .forms import ItemForm
@login_required
def new_item_owner(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user 
            item.save()
            return redirect('d_dashboard:dashboard-page')
    else:
        form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, 'd_dashboard/new_item.html', context)

# Membuat Delete Product
@login_required
def delete_item_owner(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('d_dashboard:dashboard-page')

# Membuat Edit Product
@login_required
def edit_item_owner(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.updated_by = request.user
            item.save()
        return redirect('d_dashboard:dashboard-page')
    else:
        form = ItemForm(instance=item)
        context = {
            'form': form,
            }
    return render(request, 'd_dashboard/edit_item.html', context)

# Membuat Fungsi Blog Admin
from f_blog.models import Category_blog, Blog
@login_required
def dashboard_blog_admin(request):
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
    return render(request, 'd_dashboard/dashboard_blog_admin.html', context)

# Membuat Fungsi Tambah Blog
from .forms import BlogForm
@login_required
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('d_dashboard:blog-admin')
    else:
        form = BlogForm()
    context ={
        'form': form,
    }
    return render(request, 'd_dashboard/add_blog.html', context)

# Membuat Detail Blog Admin
from f_blog.models import Category_blog, Blog
@login_required
def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'd_dashboard/blog_detail.html', context)

# Membuat Fungsi Delete Blog
@login_required
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('d_dashboard:blog-admin')

# Membuat Fungsi Edit Blog
@login_required
def edit_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('d_dashboard:blog-admin')
    else:
        form = BlogForm(instance=blog)
        context = {
            'form': form,
        }
    return render(request, 'd_dashboard/edit_blog.html', context)

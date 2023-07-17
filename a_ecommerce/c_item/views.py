from django.shortcuts import render,get_list_or_404 ,redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q



# Create your views here.
from django.http import HttpResponse


# Membuat Fungsi Item Product
from .models import Category, Item
def items(request):
    query = request.GET.get('query', '')


    category_id = request.GET.get('category',0)

    categories = Category.objects.all()

    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(descriptions__icontains=query))


    context = {
        'categories': categories,
        'items': items,
        'query': query,
        'category_id': int(category_id),
    }
    return render(request, 'c_item/items.html', context)

# Membuat Fungsi detail
def item_detail(request, pk):
    item = Item.objects.get(id=pk)

    # Membuat Related item
    related_items = Item.objects.filter(category_id=item.category,is_sold=False).exclude(pk=pk)[0:3]

    context = {
        'items': item,
        'related_items': related_items,
        }
    return render(request, 'c_item/item_detail.html', context)



# Membuat Newe Product
from . forms import ItemForm
@login_required
def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user 
            item.save()
            return redirect('c_item:items-page')
    else:
        form = ItemForm()
    context = {
        'form': form,
    }
    return render(request, 'c_item/new_item.html', context)


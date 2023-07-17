from django import forms

from c_item.models import Item
from f_blog.models import Blog

# Membuat Class Itemform
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'descriptions', 'price', 'category', 'image','create_by',]

# Membuat Class BlogForm
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content_1', 'content_2','content_3', 'category', 'image',]
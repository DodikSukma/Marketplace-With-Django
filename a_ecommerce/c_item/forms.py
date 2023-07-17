from django import forms

from .models import Item

# Membuat Class Itemform
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'descriptions', 'price', 'category', 'image','create_by',]

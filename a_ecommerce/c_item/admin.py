from django.contrib import admin

# Register your models here.

# Daftarakan ke django admin

from . models import Category, Item

admin.site.register(Category)
admin.site.register(Item)

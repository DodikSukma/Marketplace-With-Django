from django.contrib import admin

# Register your models here.
# Daftarakan ke django admin

from . models import Category_blog, Blog, Comment

admin.site.register(Category_blog)
admin.site.register(Blog)
admin.site.register(Comment)
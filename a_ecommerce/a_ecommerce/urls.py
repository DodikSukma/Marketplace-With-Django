"""
URL configuration for a_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Memanggil b_core urls
    path('', include('b_core.urls')),

    # Memanggil c_item urls
    path('items/', include('c_item.urls')),
    
    # Panggil d_dashboard urls
    path('dashboard/', include('d_dashboard.urls')),

    # Panggil f_blog urls
    path('blog/', include('f_blog.urls')),

    # Panggil g_pesan urls
    # path('pesan/', include('g_pesan.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    # Tambahkan ini jika ingin menampilkan media seperti gambar dan vidio
    # Code di atas berdasarkan apa yang sudah disetting di setting.py sebelumnya


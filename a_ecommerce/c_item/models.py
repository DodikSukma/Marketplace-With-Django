# Memanggil Model table User
from django.contrib.auth.models import User


from django.db import models
# Create your models here.


# ===================== MODELS.PY BERTUJUAN UNTUK MEMBUAT TABLE PADA DATABASE ==========================
# Membuat Table data Category product

# Membuat Class Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
# Membuat Class Item Product
class Item(models.Model):
    category        = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    descriptions    = models.TextField(blank=True, null=True)
    price           = models.FloatField()
    image           = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold         = models.BooleanField(default=False)
    create_by       = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    create_at       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Catatan Umum :
        # 1 Pastikan Semua type data sudah benar dan pastikan sudah terelasi dengan benar
        # 2 Pastikan Sudah membuat superuser jika ingin menggunakna django admin
        # 3 Pastikan Sudah menghubungkan dengan Mysql jika menggunakna mysql lakukan setting hubungan dengan sql di setting.py
        # 4 Pastikan sudah menginstall mysqlient jika ingin melakukan hubungan dengan sql
        # 5 Pastikan saat selesai membuat code table melakukan 
                    # a . python manage.py makemigrations
                    # b . python manage.py migrate

from django.db import models

# Create your models here.

# ===================== MODELS.PY BERTUJUAN UNTUK MEMBUAT TABLE PADA DATABASE ==========================
# Membuat Table data Category Blog

# Membuat Class Category_blog
class Category_blog(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

# Membuat Class Blog
class Blog(models.Model):
    category    = models.ForeignKey(Category_blog, related_name='blog', on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    content_1   = models.TextField(blank=True, null=True)
    content_2   = models.TextField(blank=True, null=True)
    content_3   = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='blog_images', blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Membuat Class Comment 
class Comment(models.Model):
    blog            = models.ForeignKey(Blog, related_name='comment', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    email           = models.EmailField(blank=True, null=True)
    content         = models.TextField(blank=True, null=True)
    date_created    = models.DateField(auto_now_add=True)
    date_updated    = models.DateField(auto_now=True)

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
# Generated by Django 4.2 on 2023-04-21 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category_blog',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-02 09:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='آدرس')),
                ('thumbnail', models.ImageField(upload_to='image/category/%Y/%m/%d/', verbose_name='تصویر')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('position', models.IntegerField(unique=True, verbose_name='موقعیت')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='آدرس')),
                ('body', ckeditor.fields.RichTextField(verbose_name='متن')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'پیش نویس'), ('published', 'انتشار')], default='draft', max_length=10, verbose_name='وضعیت')),
                ('thumbnail', models.ImageField(upload_to='image/articles/%Y/%m/', verbose_name='تصویر')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ['publish'],
            },
        ),
    ]

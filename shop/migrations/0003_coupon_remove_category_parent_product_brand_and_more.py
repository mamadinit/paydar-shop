# Generated by Django 4.2.1 on 2023-05-09 09:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_pictures_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='کد تخفیف')),
                ('valid_from', models.DateTimeField(verbose_name='معتبر از')),
                ('valid_to', models.DateTimeField(verbose_name='معتبر تا')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='مقدار تخفیف')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد های تخفیف',
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=0, max_length=100, verbose_name='برند'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_series',
            field=models.CharField(max_length=150, verbose_name='نوع پردازنده'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.category', verbose_name='دسته بندی'),
        ),
    ]

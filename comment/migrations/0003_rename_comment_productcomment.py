# Generated by Django 4.2.1 on 2023-09-15 12:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order_orderitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_comment_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='ProductComment',
        ),
    ]

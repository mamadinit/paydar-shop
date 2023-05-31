# Generated by Django 4.2.1 on 2023-05-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('confirmed', 'تایید شده'), ('awaiting_confirmation', 'در انتظار تایید')], default='awaiting_confirmation', max_length=30, verbose_name='وضعیت'),
        ),
    ]
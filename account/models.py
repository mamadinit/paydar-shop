from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from .signals import customuser_created

class CustomeUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('شماره تلفن ضروری است')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser muse have is_staff=True')
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser muse have is_superuser=True')
        
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone = models.CharField(_('phone'), max_length=11, unique=True,
    help_text =_('شماره موبال را با فرمت 09000000000 در 11 رقم وارد کنید .'),
    error_messages = {
        'unique': _("این شماره موبایل قبلا استفاده شده است ."),
        },
    )
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_(
            'مشخص می کند که آیا این کاربر تلفن را تأیید کرده است یا خیر'
        ),
    )
    otp_secret = models.CharField(max_length=64, blank=True, null=True)
    otp_counter = models.SmallIntegerField(default=0)

    objects = CustomeUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'user is {self.phone}'

post_save.connect(customuser_created, sender=User)

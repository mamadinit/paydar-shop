from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from extensions.utils import jalali_converter
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
    bank_card = models.CharField(max_length=16, verbose_name='کارت بانکی', null=True)
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

    def jpublish(self):
        return jalali_converter(self.date_joined)

    def __str__(self):
        return f'user is {self.phone}'

post_save.connect(customuser_created, sender=User)



class Address(models.Model):



    PROVINCES_CHOICES = (
        ('البرز', 'البرز'),
        ('اردبیل', 'اردبیل'),
        ('اصفهان', 'اصفهان'),
        ('آذربایجان شرقی', 'آذربایجان شرقی'),
        ('آذربایجان غربی', 'آذربایجان غربی'),
        ('بوشهر', 'بوشهر'),
        ('تهران', 'تهران'),
        ('چهارمحال و بختیاری', 'چهارمحال و بختیاری'),
        ('خراسان جنوبی', 'خراسان جنوبی'),
        ('خراسان رضوی', 'خراسان رضوی'),
        ('خراسان شمالی', 'خراسان شمالی'),
        ('خوزستان', 'خوزستان'),
        ('زنجان', 'زنجان'),
        ('سمنان', 'سمنان'),
        ('سیستان و بلوچستان', 'سیستان و بلوچستان'),
        ('فارس', 'فارس'),
        ('قزوین', 'قزوین'),
        ('قم', 'قم'),
        ('کردستان', 'کردستان'),
        ('کرمان', 'کرمان'),
        ('کرمانشاه', 'کرمانشاه'),
        ('کهگیلویه و بویراحمد', 'کهگیلویه و بویراحمد'),
        ('گلستان', 'گلستان'),
        ('گیلان', 'گیلان'),
        ('لرستان', 'لرستان'),
        ('مازندران', 'مازندران'),
        ('مرکزی', 'مرکزی'),
        ('هرمزگان', 'هرمزگان'),
        ('همدان', 'همدان'),
        ('یزد', 'یزد')
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='address')
    transferee_name = models.CharField(max_length=100, verbose_name='تحویل گیرنده')
    province = models.CharField(max_length=100, choices = PROVINCES_CHOICES, verbose_name='استان')
    city = models.CharField(max_length=100, verbose_name='شهر')
    postal_code = models.IntegerField( verbose_name='کد پستی')
    address = models.TextField(max_length=500, verbose_name='آدرس')

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها" 

    def __str__(self):
        return f'{self.province} , {self.city} , {self.address}'
    
    def get_full_address(self):
        return f'{self.province} , {self.city} , {self.address}'     
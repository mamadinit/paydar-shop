from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Attribute(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(max_length=1000, verbose_name='توضیحات')
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='زیردسته')
    title = models.CharField(max_length = 50, verbose_name = "عنوان دسته بندی")
    slug = models.SlugField(max_length = 100, unique = True, verbose_name = "اسلاگ")

class Classification(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "عنوان  طبقه بندی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title 

class Picture(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "نام فایل")
    image = models.ImageField(upload_to = "products/%Y/%m/", verbose_name='فایل')

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"


    def __str__(self):
        return self.title 

class Product(models.Model):

    title = models.CharField(max_length=150, verbose_name='نام محصول')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس')
    description = RichTextField(null = True, blank = True, verbose_name= "توضیحات")
    inventory = models.BooleanField(default=True, verbose_name='موجودی در انبار')
    price = models.IntegerField(verbose_name='قیمت')
    images = models.ManyToManyField(Picture, verbose_name = "تصاویر", related_name="images")
    category = models.ManyToManyField(Category, verbose_name = "دسته بندی", related_name="products")
    classification = models.ManyToManyField(Classification, verbose_name = 'طبقه بندی', related_name="products")
    attribute = models.ManyToManyField(Attribute, verbose_name = "مشخصات", related_name="attributes")
    processor_series = models.CharField(max_length=150, verbose_name='نام محصول')
    ram_memory = models.CharField(max_length=2, verbose_name='ظرفیت حافظه RAM')
    gpu_series = models.CharField(max_length=60, verbose_name='پردازنده گرافیکی')
    screen_size = models.CharField(max_length=10, verbose_name='اندازه صفحه نمایش')
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


    def __str__(self):
        return self.title 
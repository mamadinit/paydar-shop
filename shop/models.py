from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from extensions.utils import jalali_converter
from account.models import User, Address

# Create your models here.


class Attribute(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(max_length=1000, verbose_name='توضیحات')
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "عنوان دسته بندی")
    slug = models.SlugField(max_length = 100, unique = True, verbose_name = "اسلاگ")

    def __str__(self):
        return self.title 

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
    category = models.OneToOneField(Category, null = True, verbose_name = "دسته بندی", related_name="products", on_delete=models.SET_NULL)
    classification = models.ManyToManyField(Classification, verbose_name = 'طبقه بندی', related_name="products")
    attribute = models.ManyToManyField(Attribute, verbose_name = "مشخصات", related_name="attributes")
    brand = models.CharField(max_length=100, verbose_name='برند')
    processor_series = models.CharField(max_length=150, verbose_name='نوع پردازنده')
    ram_memory = models.CharField(max_length=2, verbose_name='ظرفیت حافظه RAM')
    gpu_series = models.CharField(max_length=60, verbose_name='پردازنده گرافیکی')
    screen_size = models.CharField(max_length=10, verbose_name='اندازه صفحه نمایش')
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


    def __str__(self):
        return self.title 
    


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name='کد تخفیف')
    valid_from = models.DateTimeField(verbose_name='معتبر از')
    valid_to = models.DateTimeField(verbose_name='معتبر تا')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='مقدار تخفیف')
    status = models.BooleanField(default=False, verbose_name='وضعیت')

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کد های تخفیف" 

    def __str__(self):
        return self.code
    

class Order(models.Model):
    STATUS_CHOICES = (
        ("paid", "پرداخت شده"),
        ("awaiting_payment", "در انتظار پرداخت"),
        ("canceled", "لغو شده")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='orders', verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = "awaiting_payment" , verbose_name='وضعیت')
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True , verbose_name='آدرس تحویل')
    delivery_date = models.DateTimeField(blank=True, verbose_name='تاریخ تحویل')
    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name='تخفیف')

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "شفارشات" 

    def delivery_date_jpublish(self):
        return jalali_converter(self.delivery_date) 

    def jpublish(self):
        return jalali_converter(self.created)     

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_discount(self):
        if self.discount:
            return int((self.discount / 100) * self.get_total_price())
        return 0 
    
    def get_total_price_by_discount(self):
        if self.discount:
            return int(self.get_total_price() - self.get_total_discount())
        return self.get_total_price()


    def __str__(self):
        return f"{self.user} - {self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = "دسته "
        verbose_name_plural = "دسته ها " 

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
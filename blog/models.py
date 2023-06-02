from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from extensions.utils import jalali_converter
from account.models import User

# Create your models here.

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status="published")
    

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length = 40, unique = True, verbose_name="عنوان")
    slug = models.SlugField(max_length = 20, unique = True, verbose_name="آدرس")
    thumbnail = models.ImageField(upload_to = "image/category/%Y/%m/%d/", verbose_name="تصویر")
    status = models.BooleanField(default = True, verbose_name="وضعیت")
    position = models.IntegerField(unique = True, verbose_name="موقعیت")

    # objects = CategoryManager()

    class Meta():
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):

    STATUS_CHOICES = (
    ("draft", "پیش نویس"),
    ("published", "انتشار")
)


    title = models.CharField(max_length = 150, verbose_name="عنوان")
    slug = models.SlugField(max_length = 20, unique = True, verbose_name="آدرس")   #use for Article URL
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, related_name = "articles", verbose_name="نویسنده")
    body = RichTextField(verbose_name="متن")
    publish = models.DateTimeField(default = timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = "draft", verbose_name="وضعیت")
    thumbnail = models.ImageField(upload_to = "image/articles/%Y/%m/", verbose_name="تصویر")
    category = models.ManyToManyField(Category, related_name = "articles", verbose_name="دسته بندی")
    # hits = models.ManyToManyField(IpAddress, through="ArticleHit", blank=True, related_name='hits')

    objects = ArticleManager()

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["publish"]


    def jpublish(self):
        return jalali_converter(self.publish)
        
    def category_to_str(self):
        return ", ".join([category.title for category in self.category.all()])    

    def __str__(self):
        return self.title

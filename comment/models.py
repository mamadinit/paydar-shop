from django.db import models
from extensions.utils import jalali_converter
from account.models import User
from shop.models import Product


class Comment(models.Model):
    STATUS_CHOICES = (
        ("confirmed", "تایید شده"),
        ("awaiting_confirmation", "در انتظار تایید"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(max_length = 30, choices = STATUS_CHOICES, default = "awaiting_confirmation" , verbose_name='وضعیت')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def jpublish(self):
        return jalali_converter(self.created)  
    
    def __str__(self):
        return f'{self.user} - {self.content}' 
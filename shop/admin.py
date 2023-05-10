from django.contrib import admin
from .models import (
    Product,
    Picture,
    Category,
    Classification, 
    Attribute, 
    Coupon,
    Order,
    OrderItem,)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Picture)

admin.site.register(Classification)
admin.site.register(Attribute)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)

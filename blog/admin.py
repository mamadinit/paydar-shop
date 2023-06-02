from django.contrib import admin
from .models import Article, Category

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "position"]
    list_editable = ["position"]

admin.site.register(Category, CategoryAdmin)
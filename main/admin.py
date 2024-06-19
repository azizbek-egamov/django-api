from django.contrib import admin
from .models import *

# Register your models here.

class ArticleAdmins(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Kitob)
class KitobInfo(ArticleAdmins):
    list_display = ('name', 'id', 'category', 'author', 'created', 'view', 'slug',)
    search_fields = ('id', 'name__icontains', 'author',)

# admin.site.register(Kitob)
@admin.register(Category)
class CategoryInfo(ArticleAdmins):
    list_display = ('name', 'id')
    
admin.site.register(BookDownloads)

from django.contrib import admin

from .models import Category, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'views', 'author', 'category')
    list_display_links = ('pk', 'title')
    readonly_fields = ('views',)

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
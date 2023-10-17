from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название категории')

    def __str__(self):
        return self.name

    def has_articles(self):
        articles = self.articles.all()
        return True if articles else False


class Article(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок статьи", unique=True)
    short_description = models.TextField(verbose_name="Краткое описание", max_length=400)
    full_description = models.TextField(verbose_name="Полное описание")
    photo = models.ImageField(verbose_name="фото", upload_to="photos/articles/")
    views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания статьи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления статьи")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', related_name="articles")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория",
                                 related_name="articles")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


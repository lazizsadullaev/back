from django.shortcuts import render, HttpResponse
from .models import Article, Category

from django.core.paginator import Paginator
# Create your views here.

def home_view(request):
    articles = Article.objects.all()
    paged = Paginator(articles, 3)
    page = request.GET.get('page')
    articles = paged.get_page(page)
    context = {
        'articles' : articles
    }
    return render(request, 'web_site/index.html', context)


def category_articles(request, category_id):
    category = Category.objects.get(pk=category_id)
    articles = category.articles.all()
    paged = Paginator(articles, 3)
    page = request.GET.get('page')
    articles = paged.get_page(page)
    context = {
        'articles': articles
    }
    return render(request, 'web_site/index.html', context)


def article_ditail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        "article": article
    }
    return render(request, "web_site/article_ditail.html", context)


def registration(request):
    return render(request, 'web_site/registration.html')

def login(request):
    return render(request, 'web_site/login.html')

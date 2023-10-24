from django.shortcuts import render, HttpResponse, redirect
from .models import Article, Category

from django.core.paginator import Paginator
from django.contrib.auth import login,logout,authenticate
from .forms import RegistrationForm, LoginForm
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
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        "form": form
    }
    return render(request, 'web_site/registration.html', context)

def llogin(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'web_site/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')

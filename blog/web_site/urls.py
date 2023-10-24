from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('categories/<str:category_id>/', views.category_articles, name='category_articles'),
    path('articles/<str:article_id>/', views.article_ditail , name='article_ditail'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.llogin, name='login')
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    category = Category.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей', 'category': category})


def get_category(request, category_number):
    news = News.objects.filter(category_id=category_number)
    category = Category.objects.get(pk=category_number)
    return render(request, 'news/category.html', {'news': news, 'category': category})

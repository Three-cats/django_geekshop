from django.shortcuts import render
import json

# Create your views here.
from mainapp.models import Product, ProductCategories


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def load_json(title):
    with open(f'mainapp/fixtures/{title}.json', 'r', encoding='utf-8') as from_json:
        return json.load(from_json)


def products(request):
    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', content)

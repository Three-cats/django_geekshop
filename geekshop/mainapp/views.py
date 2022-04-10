from django.shortcuts import render
import json

# Create your views here.


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def load_json(title):
    with open(f'mainapp/fixtures/{title}.json', 'r', encoding='utf-8') as from_json:
        return json.load(from_json)


def products(request):
    categories = load_json('categories')
    cards = load_json('cards')
    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'cards': cards
    }
    return render(request, 'mainapp/products.html', content)

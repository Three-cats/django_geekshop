from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import json

# Create your views here.
from django.views.generic import DetailView
from mainapp.models import Product, ProductCategories


def index(request):
    context = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', context)


def load_json(title):
    with open(f'mainapp/fixtures/{title}.json', 'r', encoding='utf-8') as from_json:
        return json.load(from_json)


def products(request, id_category=None, page=1):
    if id_category:
        products = Product.objects.filter(id=id_category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page=2)

    try:
        product_paginator = paginator.page(page)
    except PageNotAnInteger:
        product_paginator = paginator.page(1)
    except EmptyPage:
        product_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_paginator
    }

    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

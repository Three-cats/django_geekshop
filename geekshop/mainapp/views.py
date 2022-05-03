from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
import json

# Create your views here.
from django.views.generic import DetailView
from mainapp.models import Product, ProductCategories


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def load_json(title):
    with open(f'mainapp/fixtures/{title}.json', 'r', encoding='utf-8') as from_json:
        return json.load(from_json)


def products(request, id_category=None, page=1):
    if id_category:
        products = Product.objects.filter(id=id_category)
    else:
        products = Product.objects.all()

    pagination = Paginator(products, per_page=2)

    try:
        product_pagination = pagination.page(page)
    except PageNotAnInteger:
        product_pagination = pagination.page(1)
    except EmptyPage:
        product_pagination = pagination.page(pagination.num_pages)

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_pagination
    }
    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'

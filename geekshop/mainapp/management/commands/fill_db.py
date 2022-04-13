import json
from django.core.management.base import BaseCommand

from mainapp.models import ProductCategories, Product


def load_from_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/cat.json')
        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/product.json')
        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            prod_category = prod.get('category')
            _category = ProductCategories.objects.get(id=prod_category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

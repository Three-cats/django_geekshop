import json
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategories, Product
from authapp.models import User
from chardet import detect


def encoding_convert(file):
    with open(file, 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open(file, 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


def load_from_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='Ilnur', email='ns_ilnur@mail.ru', password='1')
        encoding_convert('mainapp/fixtures/cat.json')
        categories = load_from_json('mainapp/fixtures/cat.json')
        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        encoding_convert('mainapp/fixtures/product.json')
        products = load_from_json('mainapp/fixtures/product.json')
        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            prod_category = prod.get('category')
            _category = ProductCategories.objects.get(id=prod_category)
            prod['category'] = _category
            new_product = Product(**prod)
            new_product.save()

from django.urls import path
from mainapp.views import products, index

app_name = 'mainapp'
urlpatterns = [
    path('', products, name='products')
]

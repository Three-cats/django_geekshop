from django.urls import path

from ordersapp.views import OrderList, OrderCreate, OrderUpdate, OrderRead, OrderDelete, order_forming_complete, order_change_status, get_product_price

app_name = 'ordersapp'
urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('read/<int:pk>/', OrderRead.as_view(), name='read'),
    path('forming_complete/<int:pk>/',
         order_forming_complete, name='forming_complete'),
    path('change_status/<int:pk>/', order_change_status, name='change_status'),
    path('product/<int:pk>/price/', get_product_price, name='product_price'),
]

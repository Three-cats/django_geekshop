from django.urls import path

from adminapp.views import IndexTemplateView, UserCreateView, UserDeleteView, UserListView, UserUpdateView, admin_product_create, admin_product_delete, admin_product_update, admin_products, categories, category_create, category_delete, category_update

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users_create/', UserCreateView.as_view(), name='admin_user_create'),
    path('users_update/<int:pk>/', UserUpdateView.as_view(),
         name='admin_user_update'),
    path('users_delete/<int:pk>/', UserDeleteView.as_view(),
         name='admin_user_delete'),
    path('categories/', categories, name='categories'),
    path('category_create/', category_create, name='category_create'),
    path('category_update/<int:id>/', category_update, name='category_update'),
    path('category_delete/<int:id>/', category_delete, name='category_delete'),
    path('products/', admin_products, name='admin_products'),
    path('product_create/', admin_product_create, name='admin_product_create'),
    path('product_update/<int:id>/', admin_product_update,
         name='admin_product_update'),
    path('product_delete/<int:id>/', admin_product_delete,
         name='admin_product_delete'),
]

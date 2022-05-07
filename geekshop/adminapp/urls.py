from django.urls import path

from adminapp.views import CategoryCreateView, CategoryDeleteView, CategoryListView, CategoryUpdateView, IndexTemplateView, ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView, UserCreateView, UserDeleteView, UserListView, UserUpdateView
from django.views.i18n import set_language

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users_create/', UserCreateView.as_view(), name='admin_user_create'),
    path('users_update/<int:pk>/', UserUpdateView.as_view(),
         name='admin_user_update'),
    path('users_delete/<int:pk>/', UserDeleteView.as_view(),
         name='admin_user_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>/',
         CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/',
         CategoryDeleteView.as_view(), name='category_delete'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('product_create/', ProductCreateView.as_view(),
         name='admin_product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(),
         name='admin_product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(),
         name='admin_product_delete'),
    path('lang/', set_language, name='set_language'),
]

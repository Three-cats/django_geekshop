from django.urls import path

from adminapp.views import admin_users, categories, category_create, category_delete, category_update, index, admin_user_create, admin_user_update, admin_user_delete

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users_create/', admin_user_create, name='admin_user_create'),
    path('users_update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('users_delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('categories/', categories, name='categories'),
    path('category_create/', category_create, name='category_create'),
    path('category_update/<int:name>/', category_update, name='category_update'),
    path('category_delete/<int:name>/', category_delete, name='category_delete')
]

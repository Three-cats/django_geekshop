from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authapp.models import User
from mainapp.models import Product, ProductCategories


class UserAdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'last_name',
                  'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'price',
                  'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите наименование продукта'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Количество'
        self.fields['category'].widget.attrs['placeholder'] = 'Категория'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductProfileForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'price',
                  'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'


class CategoryRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(CategoryRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'


class CategoryProfileForm(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(CategoryProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'

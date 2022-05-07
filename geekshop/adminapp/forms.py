import hashlib
import random

from django import forms
from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import Product, ProductCategories


class UserAdminRegisterForm(UserRegisterForm):
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

        # def save(self, commit=True):
        #     user = super(UserAdminRegisterForm, self).save()
        #     user.is_active = False
        #     salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        #     user.activation_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        #     user.save()
        #     return user



class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

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
    category = forms.ModelChoiceField(queryset=ProductCategories.objects.all())
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'price',
                  'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите наименование продукта'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Цена'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Количество'
        self.fields['category'].widget.attrs['placeholder'] = 'Категория'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'

        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductProfileForm(ProductRegisterForm):
    category = forms.ModelChoiceField(
        queryset=ProductCategories.objects.all().select_related(), empty_label=None)
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'price',
                  'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


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

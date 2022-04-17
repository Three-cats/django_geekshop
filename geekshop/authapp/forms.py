from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authapp.models import User
from authapp.validator import validate_name, validate_email, validate_fl_name


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(), validators=[validate_name])

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['username'].required = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(), validators=[validate_name])
    email = forms.CharField(widget=forms.TextInput(), validators=[validate_email])
    first_name = forms.CharField(widget=forms.TextInput(), validators=[validate_fl_name])
    last_name = forms.CharField(widget=forms.TextInput(), validators=[validate_fl_name])

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py4'

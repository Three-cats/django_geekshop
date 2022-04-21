from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f"Имя пользователя не может содержать только цифры"),
            params={'value': value},
        )


def validate_email(value):
    if '@' not in value:
        raise ValidationError(
            _(f"Некорректный email"),
            params={'value': value},
        )


def validate_fl_name(value):
    if not value.isalpha():
        raise ValidationError(
            _(f"Имя и фамилия должны состоять только из букв"),
            params={'value': value},
        )

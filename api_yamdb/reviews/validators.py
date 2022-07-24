import datetime

from django.core.exceptions import ValidationError


def validate_one_to_ten_range(value):
    if value < 1 or value > 10:
        raise ValidationError(
            "%(value)s не находится в диапазоне от 1 до 10",
            params={"value": value},
        )


def validate_title_year(value):
    if value > datetime.datetime.now().year:
        raise ValidationError(f"Некорректная дата произведения: {value}")

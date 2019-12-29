
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError(
                'CPF must contains only digits',
                code='cpf_wrong_content')

    if len(value) != 11:
        raise ValidationError(
                'CPF must contains 11 digits',
                code='cpf_wrong_length')

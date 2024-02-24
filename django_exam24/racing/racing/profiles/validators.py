from django.core.exceptions import ValidationError


def validate_username(value):
    if not value.isalnum():
        raise ValidationError("Username must contain only letters, digits, and underscores!")
    return value

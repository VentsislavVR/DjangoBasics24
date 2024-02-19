from django.core.exceptions import ValidationError

def validate_profile_name(name):
    if not name[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")

def validate_plant_name(name):
    if not name.isalpha():
        raise ValidationError("Plant name should contain only letters!")

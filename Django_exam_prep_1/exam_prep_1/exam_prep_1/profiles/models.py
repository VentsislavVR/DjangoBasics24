from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep_1.profiles.validators import username_validator


# Create your models here.
class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2
    MIN_AGE = 0

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH,),
            username_validator,
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ]
    )

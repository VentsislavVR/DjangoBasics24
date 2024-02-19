
from django.core.validators import MinLengthValidator
from django.db import models

from exam_doncho.profiles.validators import validate_username


# Create your models here.

class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_username,
        ],
        null=False,
        blank=False,

    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

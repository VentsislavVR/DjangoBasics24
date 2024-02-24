from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from racing.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3

    MIN_AGE = 21

    MAX_PASSWORD_LENGTH = 20

    FIRST_NAME_MAX_LENGTH = 25
    LAST_NAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_username

        ],
        error_messages={
            "min_length": "Username must be at least 3 chars long!",
        }

    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_AGE, message="Age requirement: 21 years and above.")
        ]
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,

    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )

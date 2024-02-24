from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from racing.profiles.models import Profile

YEAR_VALIDATION_ERROR = _("Year must be between 1999 and 2030!")


class Car(models.Model):
    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    MIN_YEAR = 1999
    MAX_YEAR = 2030

    MIN_PRICE = 1.0

    class Type(models.TextChoices):
        RALLY = 'Rally'
        OPEN_WHEEL = 'Open-wheel'
        KART = 'Kart'
        DRAG = 'Drag'
        OTHER = 'Other'

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
        choices=Type.choices,
    )

    model = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ],
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(MIN_YEAR, message=YEAR_VALIDATION_ERROR),
            MaxValueValidator(MAX_YEAR, message=YEAR_VALIDATION_ERROR)
        ]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one.",
        },
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        editable=False,
        blank=True,
    )

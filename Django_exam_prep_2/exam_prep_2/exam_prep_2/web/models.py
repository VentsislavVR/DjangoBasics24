from django.core.validators import MinLengthValidator
from django.db import models

from exam_prep_2.web.validators import validate_profile_name, validate_plant_name


# Create your models here.
class Profile(models.Model):
    MAX_USERNAME_LENGTH = 10
    MIN_USERNAME_LENGTH = 2

    MAX_FIRST_LAST_NAME_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_USERNAME_LENGTH)
        ],
        )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        validators=[
            validate_profile_name
        ]
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        validators=[
            validate_profile_name
        ]
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
class Plant(models.Model):

    MAX_PLANT_TYPE_LENGTH = 14
    MAX_PLANT_NAME_LENGTH = 20
    MIN_PLANT_NAME_LENGTH = 2

    PLANT_TYPE_CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )
    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PLANT_TYPE_LENGTH,
        choices=PLANT_TYPE_CHOICES


    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PLANT_NAME_LENGTH,
        validators=[
            MinLengthValidator(MIN_PLANT_NAME_LENGTH),
            validate_plant_name
        ]
    )
    image_url = models.URLField(
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )


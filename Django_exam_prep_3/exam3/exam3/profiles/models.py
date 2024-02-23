from django.db import models

# Create your models here.
class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 15
    MAX_LAST_NAME_LENGTH = 15

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH
    )
    last_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH
    )

    budget = models.PositiveIntegerField(
        default=0
    )
from django.db import models

from exam3.profiles.models import Profile


# Create your models here.
class Expense(models.Model):
    MAX_TITLE_LENGTH = 50


    title = models.CharField(
        max_length=MAX_TITLE_LENGTH
    )
    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)



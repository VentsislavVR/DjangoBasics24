from django.core.validators import MinValueValidator
from django.db import models

from exam_prep_1.profiles.models import Profile


# Create your models here.
class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENER_NAME_LENGTH = 30
    MIN_PRICE = 0

    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=MAX_GENER_NAME_LENGTH,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(

        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE),
        ]
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        editable=False,
    )
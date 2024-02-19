from django.core.validators import MinValueValidator
from django.db import models

from exam_doncho.profiles.models import Profile
class Genre(models.TextChoices):
    GENRE_POP = 'Pop Music'
    GENRE_JAZZ= 'Jazz Music'
    GENRE_ROCK = 'Rock Music'
    GENRE_COUNTRY = 'Country Music'
    GENRE_RNB = 'R&B Music'
    GENRE_DANCE = 'Dance Music'
    GENRE_HIPHOP = 'Hip Hop Music'
    GENRE_OTHER = 'Other'

# Todo: make genre enum
# Create your models here.гит
class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MIN_PRICE = 0.0
    MAX_GENRE_LENGTH = 30

    # GENRES = (
    #     (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
    #     (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
    #     (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
    #     (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
    #     (GENRE_RNB_MUSIC, GENRE_RNB_MUSIC),
    #     (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
    #     (GENRE_HIPHOP_MUSIC, GENRE_HIPHOP_MUSIC),
    #     (GENRE_OTHER, GENRE_OTHER),
    #
    # )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Album Name',
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        unique=False,
        blank=False,
        null=False,
        verbose_name='Artist',
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        null=False,
        blank=False,
        choices=(
            Genre.choices
        ),

    )

    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )



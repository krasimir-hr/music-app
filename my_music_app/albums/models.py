from django.db import models
from django.core.validators import MinValueValidator

from my_music_app.profiles.models import Profile

class Album(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    GENRE_CHOICES = (
        ('1', 'Pop Music'),
        ('2', 'Jazz Music'),
        ('3', 'R&B Music'),
        ('4', 'Rock Music'),
        ('5', 'Country Music'),
        ('6', 'Dance Music'),
        ('7', 'Hip Hop Music'),
        ('8', 'Other'),
    )

    genre = models.CharField(
        max_length=30,
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
        validators=(
            MinValueValidator(0.0),
        )
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        
    )
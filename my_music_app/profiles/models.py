from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from my_music_app.profiles.validators import validate_username


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            validate_username,
            MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username
from django.core.exceptions import ValidationError
import re


def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
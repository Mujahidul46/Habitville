from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add additional fields here if needed, e.g. profile picture, user bio, etc.
    pass


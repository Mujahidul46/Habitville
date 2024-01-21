from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    goals = models.TextField(blank=True, null=True)



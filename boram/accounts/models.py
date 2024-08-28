from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, default='images/default.png')
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False)

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # followings = models.ManyToManyField(
    #     "self", related_name="followers", symmetrical=False
    # )

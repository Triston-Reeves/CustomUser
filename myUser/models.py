from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    displayname = models.CharField(max_length=240, default="")

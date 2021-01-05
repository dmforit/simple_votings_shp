from django.db import models
from django.contrib.auth.models import AbstractUser

# TODO name avatar files uniquely


class CustomUser(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to='images/avatars')

    def __str__(self):
        return self.username

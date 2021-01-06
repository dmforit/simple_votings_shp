import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO delete file on delete or change avatar
def path_and_rename(path, old_avatar=None):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(path, filename)
    return wrapper


class CustomUser(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to=path_and_rename('images/avatars'))

    def __str__(self):
        return self.username

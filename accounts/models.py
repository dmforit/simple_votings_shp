import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver


# TODO check avatar filesize and type
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


@receiver(models.signals.post_delete, sender=CustomUser)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=CustomUser)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).avatar
    except sender.DoesNotExist:
        return False
    try:  # check if old avatar exists
        old_file.path
    except ValueError:
        return False

    new_file = instance.avatar
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

from django.db import models
from django.utils import timezone

class Vote(models.Model):
    title = models.CharField(max_length=100)
    options = models.CharField(max_length=500)
    votes = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

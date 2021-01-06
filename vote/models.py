import uuid
import ast
from django.db import models
from django.utils import timezone


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    options = models.CharField(max_length=500)
    votes = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def get_options(self):
        options = ast.literal_eval(self.options)
        return options

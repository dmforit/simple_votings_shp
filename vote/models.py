import uuid
import ast
from django.db import models
import uuid
from django.utils import timezone


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    options = models.CharField(max_length=500)
    voters = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    def get_options(self):
        options = ast.literal_eval(self.options)
        return options

    def get_voters(self):
        voters = ast.literal_eval(self.voters)
        return voters

    def get_voter(self, index):
        voters = self.get_voters()
        return voters[index]

    def __str__(self):
        return str(self.id)

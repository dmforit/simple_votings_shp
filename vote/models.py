import uuid
import ast
from django.db import models
import uuid
from django.utils import timezone


class Vote(models.Model):
    """
    Основная модель для голосований

    :param id: индекс голосования
    :param title: название голосования
    :param vote_type: тип голосования (множественный, либо единичный)
    :param options: варианты выбора
    :param votes: проголосовавшие
    :param date: дата создания
    :param author: автор голосования


    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    vote_type = models.CharField(max_length=50)
    options = models.CharField(max_length=500)
    voters = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(default='Annonym', max_length=500)

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

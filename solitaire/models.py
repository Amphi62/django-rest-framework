from django.db import models
from django.contrib.auth.models import User

from commons.enum.DifficultyGameEnum import DifficultyGameEnum
from commons.enum.StateGameEnum import StateGameEnum


class SolitaireGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=25, choices=StateGameEnum.choices, default=StateGameEnum.INITIALIZE)
    difficulty = models.CharField(max_length=25, choices=DifficultyGameEnum.choices, default=DifficultyGameEnum.EASY)
    is_timed = models.BooleanField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    slug = models.CharField(max_length=30)

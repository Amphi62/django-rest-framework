from django.db import models


class DifficultyGameEnum(models.TextChoices):
    EASY = 'easy'
    HARD = 'hard'

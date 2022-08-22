from django.db import models


class StateGameEnum(models.TextChoices):
    IN_PROGRESS = 'in-progress'
    SURRENDER = 'surrender'
    WIN = 'win'
    LOOSE = 'loose'
    INITIALIZE = 'initialize'

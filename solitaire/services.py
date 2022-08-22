from django.contrib.auth.models import User

from commons.functions.dictionnary import get_value_or_null, get_value_or_throw_error
from solitaire.models import SolitaireGame


def create_solitaire(request, fetch=True):
    game = SolitaireGame()
    game.state = get_value_or_throw_error(request, 'state')
    game.difficulty = get_value_or_throw_error(request, 'difficulty')
    game.is_timed = get_value_or_throw_error(request, 'is_timed')
    game.start_datetime = get_value_or_throw_error(request, 'start_datetime')
    game.end_datetime = get_value_or_throw_error(request, 'end_datetime')
    game.slug = get_value_or_throw_error(request, 'slug')

    user = get_value_or_throw_error(request, 'user')
    username = get_value_or_throw_error(user, 'username')

    game.user = User.objects.get(username=username)

    if fetch:
        game.save()

    return game

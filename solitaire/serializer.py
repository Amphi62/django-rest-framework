from rest_framework import serializers

from commons.serializer.UserSerializer import UserSerializer
from .models import SolitaireGame


class SolitaireSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = SolitaireGame
        fields = ['user', 'state', 'difficulty', 'is_timed', 'start_datetime', 'end_datetime', 'slug']

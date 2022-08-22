from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import SolitaireSerializer
from .models import SolitaireGame
from .services import create_solitaire


class SolitaireViews(viewsets.ModelViewSet):
    queryset = SolitaireGame.objects.all()
    serializer_class = SolitaireSerializer

    @action(methods=['post'], detail=False, url_path='create', url_name='create')
    def create_new_solitaire(self, request, *args, **kwargs):
        if SolitaireGame.objects.filter(slug=request.data['slug']).exists():
            return Response({"error": "Already exists."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            game = create_solitaire(request.data)
        except Exception as error:
            return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(SolitaireSerializer(game).data, status=status.HTTP_201_CREATED)


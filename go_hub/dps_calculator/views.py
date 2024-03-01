from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.
class PokemonListView(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

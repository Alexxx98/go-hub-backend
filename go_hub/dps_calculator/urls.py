from rest_framework.routers import DefaultRouter
from .views import PokemonListView


router = DefaultRouter()
router.register('pokemon_list', PokemonListView)
router.register('pokemon_list/<int:pokemon_id>', PokemonListView)

urlpatterns = router.urls

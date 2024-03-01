import requests
from models import Pokemon
# from .models import Pokemon


"""
Script used to add all pokemon to the database.
Design to used only in django shell.
"""

valid_forms = ("Normal", "Origin", "Altered", "Alola", "Hisuian", "Paldea", "Attack", "Defense", "Speed", "Galarian_standard", "Galarian_zen" "Galarian")

base_url = "https://pogoapi.net/"
endpoints = {
                "stats": "/api/v1/pokemon_stats.json",
                "types": "/api/v1/pokemon_types.json",
                "current_moves": "/api/v1/current_pokemon_moves.json",
                "cp_multiplier": "/api/v1/cp_multiplier.json",
                "mega_pokemon": "/api/v1/mega_pokemon.json",
            }

moves = requests.get(base_url + endpoints["current_moves"])
types = requests.get(base_url + endpoints["types"])
mega = requests.get(base_url + endpoints["mega_pokemon"])
stats = requests.get(base_url + endpoints["stats"])
moves_data = moves.json()
types_data = types.json()
mega_data = mega.json()
stats_data = stats.json()



for stats, moves, types in zip(stats_data, moves_data, types_data):
    if moves['form'] in valid_forms:
        pokemon = Pokemon(
            pokemon_id=moves['pokemon_id'],
            name=moves['pokemon_name'],
            version=moves['form'],
            attack=stats['base_attack'],
            defense=stats['base_defense'],
            stamina=stats['base_stamina'],
            types=types['type'],
            fast_moves=moves['fast_moves'] + moves['elite_fast_moves'],
            charged_moves=moves['charged_moves'] + moves['elite_charged_moves'],
        )
        pokemon.save()

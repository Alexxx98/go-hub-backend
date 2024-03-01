from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    attack = models.IntegerField()
    defense = models.IntegerField()
    stamina = models.IntegerField()
    types = ArrayField(
        models.CharField(max_length=16),
        max_length=10,
        size=2,
    )
    fast_moves = ArrayField(
        models.CharField(max_length=16),
        max_length=10,
    )
    charged_moves = ArrayField(
        models.CharField(max_length=16),
        max_length=10,
    )

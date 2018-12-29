import random

from django.db import models
from django.db.models import CASCADE

from images.models import Image
# Create your models here.

def generate_game_id():
    return random.randint(11111, 99999)

class Game(models.Model):
    opencard1 = models.IntegerField(blank=True, null=True)
    opencard2 = models.IntegerField(blank=True, null=True)
    player_count = models.IntegerField(default=0)
    player_scores = models.CharField(max_length=255, default="[0]")
    turn = models.IntegerField(default=1)
    joinid = models.IntegerField(default=generate_game_id)

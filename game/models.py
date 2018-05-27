import random

from django.db import models
from django.db.models import CASCADE

from images.models import Image
# Create your models here.

def generate_game_id():
    return random.randint(11111, 99999)

class Game(models.Model):
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    opencard1 = models.IntegerField(blank=True, null=True)
    opencard2 = models.IntegerField(blank=True, null=True)
    p1_online = models.BooleanField(default=False)
    p2_online = models.BooleanField(default=False)
    turn = models.IntegerField(default=1)
    joinid = models.IntegerField(default=generate_game_id)

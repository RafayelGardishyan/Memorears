from django.db import models
from django.db.models import CASCADE

from images.models import Image
# Create your models here.


class Game(models.Model):
    mode = models.CharField(max_length=8)
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()
    card_image_sequence = models.ManyToManyField(Image, null=True, blank=True)

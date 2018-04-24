from django.db import models


# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)

class Image(models.Model):
    image = models.ImageField(upload_to="images")
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()

    # duner str method return player name
    def __str__(self):
        return self.name
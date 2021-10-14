from django.db import models

# Create your models here.
class Batsman(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    runs = models.IntegerField()

    def __str__(self):
        return self.name

class Bowler(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    wickets = models.IntegerField()

    def __str__(self):
        return self.name

class Stadium(models.Model):
    team = models.CharField(max_length = 255)
    ground = models.CharField(max_length = 255)

    def __str__(self):
        return self.team

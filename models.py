from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    prestige_level = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname

class HorseGame(models.Model):
    player1 = models.ForeignKey(Player, related_name='horse_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='horse_player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='horse_winner', on_delete=models.CASCADE)
    date_played = models.DateTimeField(auto_now_add=True)

class Game21(models.Model):
    players = models.ManyToManyField(Player)
    winner = models.ForeignKey(Player, related_name='twentyone_winner', on_delete=models.CASCADE)
    score_log = models.TextField(blank=True)
    date_played = models.DateTimeField(auto_now_add=True)

class DunkContest(models.Model):
    participants = models.ManyToManyField(Player)
    winner = models.ForeignKey(Player, related_name='dunk_winner', on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

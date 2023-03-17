from django.db import models

class Athlete(models.Model):
    athlete_id = models.IntegerField(primary_key=True)
    athlete_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.IntegerField()
    age = models.IntegerField()
    sport = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    class Meta:
        db_table = 'athlete'

class Leaderboard(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100)
    gold_medals = models.IntegerField()
    silver_medals = models.IntegerField()
    bronze_medals = models.IntegerField()
    total_medals = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'
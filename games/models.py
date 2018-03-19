from django.db import models
from django.urls import reverse
from django.shortcuts import render, redirect


class Games(models.Model):
    games_tour = models.CharField("Tour", primary_key=True, max_length=30, unique=True, null=False, default='0')
    games_match1 = models.CharField("Match 1", max_length=50, unique=True)
    games_match2 = models.CharField("Match 2", max_length=50, unique=True)
    games_match3 = models.CharField("Match 3", max_length=50, unique=True)

   
    def __str__(self):
        return "Games tour nmr: {}".format(self.games_tour)
    

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('games')        


    class Meta:
        verbose_name_plural = 'Games'




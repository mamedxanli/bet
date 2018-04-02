from django.db import models
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.utils import timezone


class Games(models.Model):
    games_tour = models.IntegerField("Tour", primary_key=True, unique=True, null=False, default='0')
    games_match1 = models.CharField("Match 1", max_length=50)
    games_match2 = models.CharField("Match 2", max_length=50)
    games_match3 = models.CharField("Match 3", max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)


   
    def __str__(self):
        return "Games tour nmr: {}".format(self.pk)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('games')        


    class Meta:
        verbose_name_plural = 'Games'




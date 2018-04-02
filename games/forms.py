from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from games.models import Games
from django import forms
from django.utils.translation import ugettext_lazy as _


class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = (
            'games_tour',
            'games_match1',
            'games_match2',
            'games_match3',

        )
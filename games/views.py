from coupon.models import Coupon, Games
from django.views import generic
from games.forms import GamesForm
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy



class GameCreate(generic.CreateView):
    form_class = GamesForm   
    template_name = 'games/games_form.html'

 
class GamesList(generic.ListView):
    template_name = 'games/show_games.html'

    def get(self, request, *args, **kwargs):
        return super(GamesList, self).get(request, *args, **kwargs)
        
    def get_queryset(self):
        return Games.objects.all()
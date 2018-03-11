from coupon.models import Coupon, Games
from django.views import generic
from games.forms import GamesForm
from django.shortcuts import get_object_or_404, render



class GameCreate(generic.CreateView):
    model = Games
    form_class = GamesForm


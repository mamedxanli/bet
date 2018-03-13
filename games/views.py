from coupon.models import Coupon, Games
from django.views import generic
from games.forms import GamesForm
from django.shortcuts import get_object_or_404, render



class GameCreate(generic.CreateView):
    model = Games
    form_class = GamesForm


class GamesList(generic.ListView):

    template_name = 'games/show_games.html'

    def get(self, request, *args, **kwargs):
        return super(GamesList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return Games.objects.all()
"""
    def get_queryset(self):
        # Get the travels for the user
        return Games.objects.filter(assigned_driver=self.request.user)
"""
"""
    def get_context_data(self, **kwargs):

        context = super(DriverTravelList, self).get_context_data(**kwargs)
        context.update({
            "current_time": timezone.now(),
        })
        return context
"""
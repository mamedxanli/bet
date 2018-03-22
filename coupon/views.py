from coupon.models import Coupon, Games
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render

class CouponCreate(generic.CreateView):
    form_class = CouponForm
    template_name = 'coupon/coupon_form.html'

    def get_context_data(self, **kwargs):
        context = super(CouponCreate, self).get_context_data(**kwargs)
        #set some more context below.
        latest_game = Games.objects.latest('games_tour')
        context['latest_game'] = latest_game
        return context

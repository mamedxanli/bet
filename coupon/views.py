from coupon.models import Coupon, Games
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class CouponCreate(generic.CreateView):
    form_class = CouponForm
    template_name = 'coupon/coupon_form.html'
    success_url = 'coupon_submitted/'

    def get_context_data(self, **kwargs):
        context = super(CouponCreate, self).get_context_data(**kwargs)
        #set some more context below.
        latest_game = Games.objects.latest('games_tour')
        context['latest_game'] = latest_game
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(CouponCreate, self).form_valid(form)

class CouponSubmitted(generic.TemplateView):
    pass

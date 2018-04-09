from coupon.models import Coupon, Games, WinnerCoupon
from django.views import generic
from coupon.forms import CouponForm, WinnerCouponForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.http import HttpResponse
#from coupon.models import Winners

class CouponCreate(generic.CreateView):
    form_class = CouponForm
    template_name = 'coupon/coupon_form.html'

    def get_context_data(self, **kwargs):
        context = super(CouponCreate, self).get_context_data(**kwargs)
        #set some more context below.
        latest_game = Games.objects.latest('pk')
        context['latest_game'] = latest_game
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(CouponCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('coupon_submitted', args=(self.object.pk,))


class CouponSubmitted(generic.DetailView):
    template_name = 'coupon/coupon_submitted.html'
    model = Coupon

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CouponSubmitted, self).get(request, *args, **kwargs)

    def get_coupon_id(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.object.pk
    
    def get_context_data(self, **kwargs):
        context = super(CouponSubmitted, self).get_context_data(**kwargs)
        self.object = self.get_object()
        qs = Coupon.objects.get(pk=self.object.pk)
        context = {
            'coupon': qs,
            'object': self.object,
        }
        return context

class CalcWinners(generic.CreateView):
    form_class = WinnerCouponForm
    template_name = 'coupon/calc_winners.html'

'''        
    def get(self, request, *args):
        data = 'data'
        all_coupons = Coupon.objects.filter(coupon_tour=data)
        winner_coupon = WinnerCoupon.objects.filter(pk=data)
        winning_result = [ x for x in winner_coupon.values() ]
        winners = []
        for coupon in all_coupons:
            if str(winning_result[0]['result1']) in coupon.bet1:
                if str(winning_result[0]['result2']) in coupon.bet2:
                    if str(winning_result[0]['result3']) in coupon.bet3:
                        winners.append(coupon.pk)
        return render(request, 'coupon/winners_list.html', {'winners': winners})
'''
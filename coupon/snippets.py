from coupon.models import Coupon, WinnerCoupon
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


"""
def find_winner():
    all_coupons = Coupon.objects.filter(coupon_tour=3)
    winner_coupon = WinnerCoupon.objects.filter(tour=3).values()
    winners = []
    for coupon in all_coupons:
        if str(winner_coupon.model().result1) in coupon.bet1:
            print("found bet1")
            pass
        elif str(winner_coupon.model().result2) in coupon.bet2:
            print("found bet2")
            pass
        elif str(winner_coupon.model().result3) in coupon.bet3:
            print("found bet3")
            winners += coupon.pk
        else:
            continue
    return winners
"""






def find_winner(self, request, *args, **kwargs):
    tour_number = request.GET.get('id')
    all_coupons = Coupon.objects.filter(coupon_tour=tour_number)
    winner_coupon = WinnerCoupon.objects.filter(pk=tour_number).values()
    winners = []
    for coupon in all_coupons:
        if str(winner_coupon.values_list()[0][1]) in coupon.bet1:
            if str(winner_coupon.values_list()[0][2]) in coupon.bet2:
                if str(winner_coupon.values_list()[0][3]) in coupon.bet3:
                    winners += str(coupon.pk)
        else:
            continue
    
    return HttpResponseRedirect(reverse('winners_list'))
find_winner.short_description = "Find a winner"
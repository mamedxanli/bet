from django.db import models
from games.models import Games
from django.urls import reverse, reverse_lazy
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render


def find_winner(self, request, *args):
    coupon_tour = self.tour_number
    all_coupons = Coupon.objects.filter(coupon_tour=coupon_tour)
    winner_coupon = WinnerCoupon.objects.filter(pk=coupon_tour)
    winning_result = [ x for x in winner_coupon.values() ]
    winners = []
    for coupon in all_coupons:
            if str(winning_result[0]['result1']) in coupon.bet1:
                if str(winning_result[0]['result2']) in coupon.bet2:
                    if str(winning_result[0]['result3']) in coupon.bet3:
                        winners.append(coupon.pk)
    return render(request, 'coupon/winners_list.html', {'winners': winners})
find_winner.short_description = "Find a winner"


class Coupon(models.Model):
    #This field can be made non-editable by adding editable=False to the FK arguments. 
    #In this case we made it through forms so no need for that.
    coupon_tour = models.ForeignKey(Games, on_delete=models.CASCADE)
    firstname = models.CharField("First Name", max_length=30)
    lastname = models.CharField("Surname", max_length=30)
    phone_number = models.CharField("Phone number", max_length=20)
    bet1 = models.CharField("Bet 1", max_length=3)
    bet2 = models.CharField("Bet 2", max_length=3)
    bet3 = models.CharField("Bet 3", max_length=3)
    coupon_amount = models.IntegerField("Amount", default=0, editable=False)
    publish = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Coupon {}".format(self.pk)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('coupon')
    
    @property
    def _get_coupon_amount(self):
        amount = len(self.bet1) * len(self.bet2) *len(self.bet3)
        return amount 

    def save(self, *args, **kwargs):
        self.coupon_amount = self._get_coupon_amount
        super(Coupon, self).save(*args, **kwargs)


class WinnerCoupon(models.Model):
    tour = models.ForeignKey(Games, default=0, on_delete=models.CASCADE)
    result1 = models.IntegerField("Game 1", default=3)
    result2 = models.IntegerField("Game 2", default=3)
    result3 = models.IntegerField("Game 3", default=3)

    def __str__(self):
        return "Results for tour {}".format(self.tour)
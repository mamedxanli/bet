from django.contrib import admin
from coupon.models import Coupon, Games, WinnerCoupon
from coupon.snippets import find_winner
from django.db import models


@admin.register(Coupon)
class FindWinner(admin.ModelAdmin):
    coupon_tour = models.CharField('Please, specify tour number for coupons to be selected!')
    winner_tour = models.CharField('Please, specify tour number for winning coupons!')

    actions = [find_winner]
    

admin.site.register(Games)
admin.site.register(WinnerCoupon)


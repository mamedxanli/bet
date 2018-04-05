from django.contrib import admin
from coupon.models import Coupon, Games, WinnerCoupon
from coupon.snippets import find_winner
from django.db import models


@admin.register(Coupon)
class FindWinner(admin.ModelAdmin):
    #On admin page of Coupon we can visualize properties using the following syntax:
    list_display = ['id', 'coupon_tour', 'coupon_amount', 'firstname', 'lastname', 'phone_number']
    #Here we add new function to action drop down for changing coupon
    actions = [find_winner]

   

admin.site.register(Games)
admin.site.register(WinnerCoupon)


from django.contrib import admin
from coupon.models import Coupon, Games, WinnerCoupon

admin.site.register(Coupon)
admin.site.register(Games)
admin.site.register(WinnerCoupon)
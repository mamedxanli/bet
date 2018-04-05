from django.contrib import admin
from coupon.models import Coupon, Games, WinnerCoupon
from django.db import models


admin.site.register(Games)
admin.site.register(WinnerCoupon)


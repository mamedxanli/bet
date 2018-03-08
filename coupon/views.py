from django.shortcuts import render
from coupon.models import Coupon
from django.views import generic
from coupon.forms import CouponForm


class CouponCreate(generic.CreateView):
    model = Coupon
    form_class = CouponForm


class EmptyCoupon(generic.ListView):
    model = Coupon

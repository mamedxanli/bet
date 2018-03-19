from coupon.models import Coupon, Games
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render

class CouponCreate(generic.CreateView):
    #if template name is not specified here, then default name coupon_form will be used.
    model = Coupon
    form_class = CouponForm
    template_name = 'coupon/some_name.html'


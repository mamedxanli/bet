from django.shortcuts import render
from coupon.models import Coupon
from django.views import generic
from coupon.forms import CouponForm
from django.shortcuts import get_object_or_404, render


class CouponCreate(generic.CreateView):
    model = Coupon
    form_class = CouponForm


class EmptyCoupon(generic.ListView):
    model = Coupon


def show_coupon(request):
    coupon = get_object_or_404(Coupon)
    return render(request, 'coupon/coupon_list.html', {'coupon': coupon})

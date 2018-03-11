from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from coupon.models import Coupon
from django import forms
from django.utils.translation import ugettext_lazy as _


class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = (
        'coupon_tour',
        'firstname',
        'lastname',
        'phone_number',
        'coupon_id',
        'match1',
        'match2',
        'match3',
        'bet1',
        'bet2',
        'bet3',


        )

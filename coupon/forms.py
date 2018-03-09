from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from coupon.models import Coupon
from django import forms

class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = (
        'firstname',
        'lastname',
        'phone_number',
        'coupon_id',
        'match1',
        'match2',
        'match3',
        'match4',
        'match5',
        'match6',
        'match7',
        'match8',
        'match9',
        'match10',
        'match11',
        'match12',
        )

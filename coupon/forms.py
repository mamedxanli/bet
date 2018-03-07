from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from coupon.models import Coupon

class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = (
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
        betfields = (
            'bet1',
            'bet2',
            'bet3',
            'bet4',
            'bet5',
            'bet6',
            'bet7',
            'bet8',
            'bet9',
            'bet10',
            'bet11',
            'bet12',
        )

from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from coupon.models import Coupon, Games
from django import forms
from django.utils.translation import ugettext_lazy as _


class GameForm(ModelForm):
    class Meta:
        model = Games
        fields = (
            'games_tour',
            'games_match1',
            'games_match2',
            'games_match3',

        )

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

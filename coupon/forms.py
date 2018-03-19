from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from .models import Coupon, Games
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
        'bet1',
        'bet2',
        'bet3',
        )
    
    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        queryset=Games.objects.latest('games_tour')
        self.initial['coupon_tour'] = queryset
        self.fields['coupon_tour'].widget.attrs['disabled'] = True

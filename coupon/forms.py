from django.contrib import admin
from .models import Coupon, Games
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import (ModelForm, ValidationError, CharField, BooleanField,
    widgets)


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
        queryset=Games.objects.latest('pk')
        self.initial['coupon_tour'] = queryset

    def clean_coupon_tour(self):
        """
        Clean the coupon_tour field and check if it is valid
        """
        data = self.cleaned_data['coupon_tour']
        if data != Games.objects.latest('pk'):
            raise ValidationError("Wrong tour")
        return data



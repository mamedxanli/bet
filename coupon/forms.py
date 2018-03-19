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
    
    """
    def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    if not self.instance.actual_start_time:
        self.initial['actual_start_time'] = self.instance.plan_start_time
    """
    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        queryset=Games.objects.latest('games_tour')
        self.initial['coupon_tour'] = queryset
        self.fields['coupon_tour'].widget.attrs['disabled'] = True
    """
    def get_context_data(self, **kwargs):
        context = super(CouponCreate, self).get_context_data(**kwargs)
        #set some more context below.
        context['match1'] = 'bar'
        return context
    """
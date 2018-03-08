from django.contrib import admin
from django.forms import (ModelForm, ValidationError, CharField)
from coupon.models import Coupon
from django import forms

class CouponForm(forms.Form):
    match1 = forms.CharField(label="Match1", max_length=100)



"""
Example for template:
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>

"""

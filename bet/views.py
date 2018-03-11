from django.views import generic
from django.shortcuts import render



class HomePage(generic.TemplateView):
    template_name = "bet/index.html"
"""
class CouponView(generic.TemplateView):
    template_name = "coupon/coupon_form.html"

class HomePage(generic.TemplateView):
    template_name = "coupon/games_form.html"

"""
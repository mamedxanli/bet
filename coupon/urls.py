from django.conf.urls import url
from coupon import views, models
from django.urls import path
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^$', views.CouponCreate.as_view(), name='coupon'),
    url(r'^coupon_submitted/(?P<pk>\d+)/$', views.CouponSubmitted.as_view(), name='coupon_submitted'),
    url(r'^calc_winners/$', views.CalcWinners.as_view(), name='calc_winners'),
              ]

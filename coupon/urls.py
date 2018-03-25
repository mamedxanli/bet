from django.conf.urls import url
from coupon import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.CouponCreate.as_view(), name='coupon'),
    url(r'^coupon_submitted/$', TemplateView.as_view(template_name='coupon/coupon_submitted.html'), name='coupon_submitted'),
              ]

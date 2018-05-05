from django.conf.urls import url
from coupon import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'coupon'
urlpatterns = [
    url(r'^$', views.CouponCreate.as_view(), name='coupon'),
    url(r'^coupon_submitted/(?P<pk>\d+)/$', views.CouponSubmitted.as_view(), name='coupon_submitted'),
              ]

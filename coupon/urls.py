from django.conf.urls import url
from coupon import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.CouponCreate.as_view(), name='coupon'),
              ]

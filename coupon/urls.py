from django.conf.urls import url
from coupon.views import EmptyCoupon
from coupon import views

urlpatterns = [
    url(r'^$', views.EmptyCoupon.as_view(), name='coupon'),
              ]

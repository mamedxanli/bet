from django.conf.urls import url
from coupon import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.CouponCreate.as_view(), name='coupon'),
    #url(r'^post_coupon/(?P<pk>\d+)/$', views.post_coupon, name='post_coupon'),
    #url(r'^post_coupon/(?P<pk>\d+)/$', views.post_coupon, name='post_coupon'),

              ]

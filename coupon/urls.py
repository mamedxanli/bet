from django.conf.urls import url
from coupon.views import EmptyCoupon
from coupon import views
from django.urls import path


app_name = 'coupon'
urlpatterns = [
    url(r'^$', views.EmptyCoupon.as_view(), name='coupon'),
    path('<coupon>/', views.show_coupon, name='show_coupon')
              ]

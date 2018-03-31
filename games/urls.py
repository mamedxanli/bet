from django.conf.urls import url
from games import views
from django.urls import path
from django.views.generic import edit


urlpatterns = [
    url(r'^$', views.GameCreate.as_view(), name='games'),
    url(r'^games_list/$', views.GamesList.as_view()),
    url(r'^games_detail/(?P<pk>\d+)/$', views.GamesDetail.as_view(), name='games_detail'),
    #url(r'^games_coupons/(?P<pk>\d+)/$', views.GamesCoupons.as_view(), name='games_coupons'),
              ]
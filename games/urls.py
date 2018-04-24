from django.conf.urls import url
from games import views
from django.urls import path
from django.views.generic import edit

app_name = 'games'
urlpatterns = [
    url(r'^$', views.GameCreate.as_view(), name='games'),
    url(r'^games_list/$', views.GamesList.as_view()),
    url(r'^games_detail/(?P<pk>\d+)/$', views.GamesDetail.as_view(), name='games_detail'),
              ]
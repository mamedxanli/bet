from django.conf.urls import url
from games import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.GameCreate.as_view(), name='games'),
    url(r'^games_list/$', views.GamesList.as_view(), name='games-list'),
              ]
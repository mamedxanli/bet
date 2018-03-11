from django.conf.urls import url
from games import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.GameCreate.as_view(), name='games'),
              ]
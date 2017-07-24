from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_playlist, name='new_playlist'), #replace with homepage
    url(r'^(?P<playlist_id>[0-9]+)/$', views.result, name='result'), #each users playlist , attempting to make it the full link was an awful idea
]
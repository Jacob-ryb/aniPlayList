from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #replace with homepage
    url(r'^(?P<playlist_id>[0-9]+)/$', views.results, name='results'), #each users playlist , attempting to make it the full link was an awful idea
]
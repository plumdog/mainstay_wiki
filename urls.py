from django.conf.urls import patterns, url
from . import views

PREFIX = 'wiki'

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^/page/(?P<title>[\w]+)$', views.page, name='page'))

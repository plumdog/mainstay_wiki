from django.conf.urls import patterns, url
from . import views

PREFIX = 'wiki'

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^/page/(?P<title>[\w|\W]+)$', views.page, name='page'),
    url(r'^/add/$', views.add_page, name='add_page'),
    url(r'^/edit/(?P<title>[\w|\W]+)$', views.edit_page, name='edit_page'),
    url(r'^/search/(?P<terms>[\w|\W]+)$', views.search, name='search'),
    url(r'^/search/$', views.search, name='search'))

""" URLs for Posts """
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'easyblog.views.posts',
    url(r'^$',
        'posts_index', 
        name='easyblog_post_archive_index'),
    url(r'^page/(?P<page>\d+)/$',
        'posts_index', 
        name='easyblog_post_archive_index_paginated'),
    url(r'^(?P<year>\d{4})/$',
        'posts_by_year', 
        name='easyblog_post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'posts_by_month', 
        name='easyblog_post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'posts_by_day', 
        name='easyblog_post_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'post_detail', 
        name='easyblog_post_archive_detail'),
    url(r'^(?P<object_id>\d+)/$',
        'post_byid',
        name='easyblog_post_byid'),
    )

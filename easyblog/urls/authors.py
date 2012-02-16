from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns


urlpatterns = patterns('easyblog.views.authors',                      
                       url(r'^(?P<username>[.+-@\w]+)/$', 'author_detail',
                           name='easyblog_author_detail'),
                       url(r'^(?P<username>[.+-@\w]+)/page/(?P<page>\d+)/$',
                           'author_detail',
                           name='easyblog_author_detail_paginated'),
                       )

""" URLs for Categories """

from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from easyblog.models import Category

category_conf = {'queryset': Category.objects.all()}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^$', 'object_list',
                           category_conf, 'easyblog_category_list'),
                       )

urlpatterns += patterns('easyblog.views.categories',
                        url(r'^(?P<path>[-\/\w]+)/page/(?P<page>\d+)/$',
                            'category_detail',
                            name='easyblog_category_detail_paginated'),
                        url(r'^(?P<path>[-\/\w]+)/$', 'category_detail',
                            name='easyblog_category_detail'),
                        )

from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from easyblog.views.posts import archive_index_view, archive_month_view, archive_year_view, archive_day_view, date_detail_view

#TODO Can I reduce each of these into a single regexp for both paginated and non-paginated view?
urlpatterns = patterns(
    '',
    url(r'^$', archive_index_view,
        name='easyblog_post_archive_index'),
    url(r'^archive/$', archive_index_view,
        name='easyblog_post_archive_index'),
    url(r'^archive/page/(?P<page>\d+)/$', archive_index_view,        
        name='easyblog_post_archive_index_paginated'),
    url(r'^archive/(?P<year>\d{4})/$', archive_year_view,        
        name='easyblog_post_archive_year'),
    url(r'^archive/(?P<year>\d{4})/page/(?P<page>\d+)/$', archive_year_view,        
        name='easyblog_post_archive_year_paginated'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', archive_month_view,    
        name='easyblog_post_archive_month'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/page/(?P<page>\d+)/$', archive_month_view,    
        name='easyblog_post_archive_month_paginated'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', archive_day_view,    
        name='easyblog_post_archive_day'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/page/(?P<page>\d+)/$', archive_day_view,    
        name='easyblog_post_archive_day_paginated'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\w[\-\w]*)/$', date_detail_view, 
        name='easyblog_post_detail'),
)


"""                    
url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
    'post_detail', 
    name='easyblog_post_detail'),
url(r'^(?P<object_id>\d+)/$',
    'post_byid',
    name='easyblog_post_byid'),   
"""

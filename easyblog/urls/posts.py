""" URLs for Posts """
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

from easyblog import settings
from easyblog.models import Post

archive_index_view = ArchiveIndexView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    template_name='easyblog/posts/archive_index.html'
)

archive_year_view = YearArchiveView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    make_object_list=True,
    template_name='easyblog/posts/archive_year.html'
)

archive_month_view = MonthArchiveView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    template_name='easyblog/posts/archive_month.html'                              
)

urlpatterns = patterns(
    'easyblog.views.posts',
    url(r'^$', archive_index_view,
        name='easyblog_post_archive_index'),
    url(r'^page/(?P<page>\d+)/$', archive_index_view,
        name='easyblog_post_archive_index_paginated'),
    url(r'^(?P<year>\d{4})/$', archive_year_view,        
        name='easyblog_post_archive_year'),
    url(r'^(?P<year>\d{4})/page/(?P<page>\d+)/$', archive_year_view,        
        name='easyblog_post_archive_year_paginated'),    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'posts_by_month', 
        name='easyblog_post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'posts_by_day', 
        name='easyblog_post_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'post_detail', 
        name='easyblog_post_detail'),
    url(r'^(?P<object_id>\d+)/$',
        'post_byid',
        name='easyblog_post_byid'),
)

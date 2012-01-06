from django.conf.urls import patterns,  url

urlpatterns = patterns('easyblog.views',    
    url(r'^$', 'index'),     
    url(r'^posts/(?P<post_id>\d+)/$', 'detail'),  
    url(r'^tags/(?P<tag_name>\w+)/$', 'tagsearch')    
)

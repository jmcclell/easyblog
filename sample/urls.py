from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url('^markdown/', include('django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),       
    url(r'^', include('easyblog.urls')))
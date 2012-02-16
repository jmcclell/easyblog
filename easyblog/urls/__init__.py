from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    '',
    url(r'^author/', include('easyblog.urls.authors')),
    url(r'^category/', include('easyblog.urls.categories')),
    url(r'^', include('easyblog.urls.posts')),
)

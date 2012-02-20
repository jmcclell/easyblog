"""Views for Zinnia entries"""
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.date_based import archive_year
from django.views.generic.date_based import archive_month
from django.views.generic.date_based import archive_day
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.date_based import object_detail


from easyblog import settings
from easyblog.models import Post


def posts_by_day(request, year, month, day, page):
    posts = Post.live.all().order_by('-publish_date')
   
    return archive_day(request, year, month, day, posts,
                         date_field='publish_date',
                          num_latest=settings.POSTS_PER_PAGE,
                          template_name='easyblog/posts/archive.html',
                          allow_future=settings.ALLOW_FUTURE,
                          allow_empty=settings.ALLOW_EMPTY,
                          paginate_by=settings.POSTS_PER_PAGE,
                          make_object_list=True,
                          page=page)
    
def posts_by_month(request, year, month, page):
    posts = Post.live.all().order_by('-publish_date')
   
    return archive_month(request, year, month, posts,
                         date_field='publish_date',
                          num_latest=settings.POSTS_PER_PAGE,
                          template_name='easyblog/posts/archive.html',
                          allow_future=settings.ALLOW_FUTURE,
                          allow_empty=settings.ALLOW_EMPTY,
                          paginate_by=settings.POSTS_PER_PAGE,
                          make_object_list=True,
                          page=page)
    
def posts_by_year(request, year,page):
    posts = Post.live.all().order_by('-publish_date')
    return archive_year(request, year, posts, date_field='publish_date',
                     num_latest=settings.POSTS_PER_PAGE,
                      template_name='easyblog/posts/archive.html',
                      allow_future=settings.ALLOW_FUTURE,
                      allow_empty=settings.ALLOW_EMPTY,
                      paginate_by=settings.POSTS_PER_PAGE,
                      make_object_list=True,
                      page=page)

def posts_index(request, page=None):
    #posts = Post.live.all().order_by('-publish_date')
    posts = Post.objects.all().order_by('-publish_date')
   
    return archive_index(request, posts, date_field='publish_date',
                         num_latest=settings.POSTS_PER_PAGE,
                          template_name='easyblog/posts/archive.html',
                          allow_future=settings.ALLOW_FUTURE,
                          allow_empty=settings.ALLOW_EMPTY,)
    
def post_detail(request):
    posts = Post.live.all().order_by('-publish_date')
    return object_detail(request, posts, date_field='publish_date',
                         num_latest=settings.POSTS_PER_PAGE,
                          template_name='easyblog/posts/archive.html',
                          allow_future=settings.ALLOW_FUTURE,
                          paginate_by=settings.POSTS_PER_PAGE,
                          month_format='%m',)


def post_byid(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return redirect(post, permanent=True)

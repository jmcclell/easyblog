from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView

from easyblog import settings
from easyblog.models import Post

class PostArchiveIndexView(ArchiveIndexView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostArchiveIndexView, self).get_context_data(**kwargs)
        context.update({'url_extra_kwargs': self.kwargs})
        return context

class PostYearArchiveView(YearArchiveView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostYearArchiveView, self).get_context_data(**kwargs)
        context.update({'url_extra_kwargs': self.kwargs})
        return context
    
class PostMonthArchiveView(MonthArchiveView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostMonthArchiveView, self).get_context_data(**kwargs)
        context.update({'url_extra_kwargs': self.kwargs})
        return context
    
class PostDayArchiveView(DayArchiveView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDayArchiveView, self).get_context_data(**kwargs)
        context.update({'url_extra_kwargs': self.kwargs})
        return context
    
archive_index_view = PostArchiveIndexView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    template_name='easyblog/posts/archive_index.html'
)

archive_year_view = PostYearArchiveView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    make_object_list=True,
    template_name='easyblog/posts/archive_year.html'
)

archive_month_view = PostMonthArchiveView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    template_name='easyblog/posts/archive_month.html',    
    month_format='%m'                 
)

archive_day_view = PostDayArchiveView.as_view(
    date_field='publish_date',
    paginate_by=settings.POSTS_PER_PAGE,            
    allow_empty=True,
    queryset=Post.live.all(),
    context_object_name='posts',
    template_name='easyblog/posts/archive_day.html',    
    month_format='%m'                 
)

date_detail_view = DateDetailView.as_view(
    date_field='publish_date',
    queryset=Post.live.all(),
    context_object_name='post',
    template_name='easyblog/posts/detail.html',
    month_format='%m'                             
)
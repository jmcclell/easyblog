"""Views for Zinnia authors"""
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from easyblog.models import Author
from easyblog import settings

def author_detail(request, username, page=None, **kwargs):
    """Display the entries of an author"""
    extra_context = kwargs.pop('extra_context', {})

    author = get_object_or_404(Author, username=username)
    #if not kwargs.get('template_name'):
    #    kwargs['template_name'] = template_name_for_entry_queryset_filtered(
    #        'author', author.username)

    extra_context.update({'author': author})
    kwargs['extra_context'] = extra_context

    return object_list(request, queryset=author.live_posts,
                       paginate_by=settings.POSTS_PER_PAGE, page=page,
                       **kwargs)

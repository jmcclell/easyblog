""" EasyBlog Category Views """

from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list

from easyblog.models import Category
from easyblog import settings


def get_category_or_404(path):
    """Retrieve a Category by a path"""
    path_bits = [p for p in path.split('/') if p]
    return get_object_or_404(Category, slug=path_bits[-1])


def category_detail(request, path, page=None, **kwargs):
    extra_context = kwargs.pop('extra_context', {})

    slug = [p for p in path.split('/') if p][-1]
    category = get_object_or_404(Category, slug=slug)
    #if not kwargs.get('template_name'):
        #kwargs['template_name'] = template_name_for_entry_queryset_filtered(
        #   'category', category.slug)

    extra_context.update({'category': category})
    kwargs['extra_context'] = extra_context

    return object_list(request, queryset=category.live_posts,
                       paginate_by=settings.POSTS_PER_PAGE, page=page,
                       **kwargs)

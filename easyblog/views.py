import logging 

from urllib import unquote

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


from easyblog.models import Post, Tag

logger = logging.getLogger('easyblog.views') 

def index(request):    
    post_list = Post.objects.all().order_by('-publish_date')
    paginator = Paginator(post_list, 3)
    
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render_to_response('easyblog/posts/index.html',
                              {'posts': posts},
                              context_instance=RequestContext(request))
    

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('easyblog/posts/detail.html',
                              {'post': post},
                              context_instance=RequestContext(request))
    
def tagsearch(request, tags):
    # URL decode the tag
    logger.debug("Received the following tag parameter: %s" % tags)
    tags = unquote(tags)
    logger.debug("Unencoded parameter: %s" % tags)
    tags = tags.split('+')
    logger.debug("Split list: %s" % ", ".join(tags))
    
    tag_models = Tag.objects.filter(name__in=tags)

    #tag = get_object_or_404(Tag, name__exact=tag_name)
    tagged_posts_list = Post.objects.filter(tags = tag_models)
    paginator = Paginator(tagged_posts_list, 3)
        
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render_to_response('easyblog/posts/tagged.html',
                              {'posts': posts,
                               'tags' : tags},
                              context_instance=RequestContext(request))
    
    
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from easyblog.managers import PostLiveManager, PostStatusLiveManager


class MyTaggableManager(TaggableManager):
    """
    This class is necessary so that django-dilla can spam the db for testing.
    It serves no other purpose.
    
    #TODO A better approach might be to fork django-taggit and add this method
          to the codebase
    """
    def get_internal_type(self):
        return "ManyToManyField"
    
    
    
class Author(User):    
    """ Proxy model representing the author, extending User """
    
    objects = models.Manager()
        
    @property
    def live_posts(self):
        """Return only the entries published"""
        return Post.live.filter(author__pk=self.pk)

    
    @models.permalink
    def get_absolute_url(self):
        return ('easyblog_author_detail', (self.username,))
    
    class Meta:
        proxy = True

def get_default_post_status():
    return PostStatus.objects.filter(default=True)[:1].get()

class PostStatus(models.Model):    
    """ Status of the post, eg: published, draft, etc. """
    
    # Manager which will return only statuses which are "live"
    objects = models.Manager()
    live_statuses = PostStatusLiveManager()
    
    name = models.CharField(max_length=255, unique=True)    
    ordering = models.IntegerField(null=False, blank=False, unique=True)
    is_live = models.BooleanField(default=False, null=False, blank=True)
    default = models.BooleanField(default=False, null=False, blank=False)
    
    def save(self, *args, **kwargs):        
        if self.default is True:
            # Ensure no other PostStatus is set as default
            PostStatus.objects.exclude(pk=self.pk).update(default=False)
        else:
            # One PostStatus must always be default. We can't set this to false without setting another to true.
            if not PostStatus.objects.exists(default=True):
                raise Exception("At least one PostStatus must be set as Default at all times")
                
        super(PostStatus, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name    
    
    class Meta:
        ordering = ["ordering"]
        verbose_name = 'post statuses'
        verbose_name_plural = 'post statuses'

class Category(models.Model):
    
    objects = models.Manager()
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               verbose_name='parent category',
                               related_name='children')

    @property
    def tree_path(self):
        if self.parent:
            return '%s/%s' % (self.parent.tree_path, self.name)
        else:
            return self.name
        
    @property
    def tree_path_slug(self):
        if self.parent:
            return '%s/%s' % (self.parent.tree_path, self.slug)
        else:
            return self.slug
        
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('easyblog_category_detail', (self.tree_path_slug,))

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    
         
class Post(models.Model):
    
    objects = models.Manager()
    live = PostLiveManager()
    #related = managers.PostRelatedManager
    
    title = models.CharField(max_length=255)
    #image = models.ImageField(upload_to=settings.UPLOAD_DIR, blank=True)
    slug = models.SlugField(max_length=255, unique_for_date='publish_date')
    category = models.ForeignKey(Category, null=True, blank=True)
    body = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(Author)    
    created_on = models.DateTimeField('created on', null=False, blank=True, editable=False)
    modified_on = models.DateTimeField('last modified on', null=True,
                                     blank=True, editable=False)
    publish_date = models.DateTimeField('publish date', db_index=True,
                                        null=True, blank=True, 
                                        default=timezone.now())
    status = models.ForeignKey(PostStatus, null=False, blank=True, default=get_default_post_status)
    follows = models.ForeignKey('self', null=True, blank=True, unique=True, verbose_name='previous post in series')    
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = MyTaggableManager(blank=True)
    
   
    def is_edited(self):        
        return not self.modified_on is None
    is_edited.short_description = 'edited?'
    is_edited.boolean = True
    
    def is_live(self):
        return self.status.is_live and self.publish_date <= timezone.now()
    is_live.short_description = 'live?'
    is_live.boolean = True
    
    @models.permalink
    def get_absolute_url(self):
        #return ('easyblog_post_detail', (), {
        #    'year': self.created_on.strftime('%Y'),
        #    'month': self.created_on.strftime('%m'),
        #    'day': self.created_on.strftime('%d'),
        #    'slug': self.slug})
        return ('easyblog_post_detail', (), {
            'year': self.publish_date.strftime('%Y'),
            'month': self.publish_date.strftime('%m'),
            'day': self.publish_date.strftime('%d'),
            'slug': self.slug})
    get_absolute_url.short_description = 'URL'
    
    
    #@TODO Implement related in such a way that it returns the top X posts with the most tags in common
    def get_related(self, count=5):
        pass
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_on = timezone.now()
        else:
            self.modified_on = timezone.now()
                            
        super(Post, self).save(*args, **kwargs)
     
    def __unicode__(self):
        return self.title

    
    class Meta:
        ordering = ["-publish_date"]
        get_latest_by = "publish_date"
    



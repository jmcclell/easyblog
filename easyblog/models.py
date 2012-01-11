from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

from easyblog import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
    
    class Dilla():
        field_extras = {
            'name': {
                'word_count':1,
                'spaces':False                
            }
        }

# Is this really the python way of doing it? There does not seem to be
# static method support, so putting this in PostStatus doesn't work as
# I would expect. @TODO Investigate further
def get_default_status():
        return PostStatus.objects.get(id=settings.DEFAULT_POST_STATUS_ID)
        
class PostStatus(models.Model):    
    name = models.CharField(max_length=50, unique=True)    
    ordering = models.IntegerField(default=0)
    is_live = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["ordering"]
    
    class Dilla():
        skip_model=True
           
class Post(models.Model):
    title = models.CharField(max_length=255, unique_for_date='publish_date')
    slug = models.SlugField(max_length=255, unique_for_date='publish_date')
    body = models.TextField()
    user = models.ForeignKey(User, verbose_name='owner')    
    created_on = models.DateTimeField('created on', auto_now_add=True)
    modified_on = models.DateTimeField('last modified on', null=True,
                                     blank=True, auto_now=True)
    publish_date = models.DateTimeField('publish date', db_index=True,
                                        null=True, blank=True, 
                                        default=timezone.now)    
    status = models.ForeignKey(PostStatus, null=False, blank=True, default=get_default_status)
    follows = models.ForeignKey('self', null=True, blank=True, unique=True, verbose_name='previous post in series')
    tags = models.ManyToManyField(Tag, db_index=True, null=True, blank=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
   
    def is_edited(self):
        return not self.modified_on == self.created_on
    is_edited.short_description = 'edited?'
    is_edited.boolean = True
    
    def is_live(self):
        return self.status.is_live and self.publish_date <= timezone.now()
    is_live.short_description = 'live?'
    is_live.boolean = True
    
    #@TODO Implement related in such a way that it returns the top X posts with the most tags in common
    def get_related(self, count=5):
        pass
     
    def __unicode__(self):
        return self.title
    
    def get_url(self):
        return "/%s/%s" % (self.publish_date.strftime("%Y/%b/%d"),
                           self.slug)
    
    class Meta:
        ordering = ["publish_date"]
        get_latest_by = "publish_date"
        
    class Dilla():
        field_extras = {
            'follows': {
                'generator': None              
            }
        }
        
    



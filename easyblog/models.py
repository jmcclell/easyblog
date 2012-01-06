from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __unicode__(self):
        return self.name
    
class PostStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)    
    ordering = models.IntegerField(default=0)
    is_live = models.BooleanField(default=False, blank=True)
    
    def __unicode__(self):
        return self.name
           
class Post(models.Model):
    title = models.CharField(max_length=255, unique_for_date='publish_date')
    slug = models.CharField(max_length=255, unique_for_date='publish_date')
    body = models.TextField()
    user = models.ForeignKey(User, verbose_name='owner')    
    created_on = models.DateTimeField('created on', auto_now_add=True)
    modified_on = models.DateTimeField('last modified on', null=True,
                                     blank=True, auto_now=True)
    publish_date = models.DateTimeField('publish date', db_index=True,
                                        null=True, blank=True, 
                                        default=timezone.now)
    
    status = models.ForeignKey(PostStatus)
    follows = models.ForeignKey('self', null=True, blank=True, unique=True, verbose_name='previous post in series')
    related = models.ManyToManyField('self', null=True, blank=True, verbose_name='related posts')
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
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ["publish_date"]
        get_latest_by = "publish_date"
        
    



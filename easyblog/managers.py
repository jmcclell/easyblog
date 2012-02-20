""" EasyBlog Model Managers and helpers """
from django.utils import timezone
from django.db import models

# Because of a circular dependency, we can't import models specifically
import easyblog

class PostStatusLiveManager(models.Manager):
    def get_query_set(self):
        """Return PostStatus objects which are defined as "live" (eg: Published) """
        return super(PostStatusLiveManager, self).get_query_set().filter(
            is_live=True
        )

class PostLiveManager(models.Manager):
    def get_query_set(self):
        """Return posts that are live (ie: their PostStatus is a Live status and their publish date has past)"""
        return super(PostLiveManager, self).get_query_set().filter(status__in=easyblog.models.PostStatus.live_statuses.all(),
                                                                   publish_date__lte=timezone.now())



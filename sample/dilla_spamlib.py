from django.utils import timezone
from dilla import spam, spammers
import random

#@spam.strict_handler('easyblog.Post.title')
#def get_blog_post_title(record, field):
#    return random.choice(string.ascii_letters)

@spam.global_handler('DateField')
@spam.global_handler('TimeField')
@spam.global_handler('DateTimeField')
def random_datetime_tz_aware(record, field):
    """
    Calculate random datetime object between last and next month.
    Django interface is pretty tollerant at this point, so three
    decorators instead of three handlers here.
    """
    # 1 month ~= 30d ~= 720h ~= 43200min
    random_minutes = random.randint(-43200, 43200)

    return timezone.now() + timezone.timedelta(minutes=random_minutes)

@spam.strict_handler('easyblog.models.Post.status')
def get_default_post_status(record, field):
    weighted_choices = [1, 1, 1, 2]
    return random.choice(weighted_choices)

@spam.strict_handler('easyblog.models.Post.tags')
def get_post_tags(record, field):
    return spammers.random_words(record, field)
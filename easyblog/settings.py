"""EasyBlog Settings"""
from django.conf import settings

"""
This title will always show up in your title as the first part. If you want
a separator, add it here. Templates will automatically insert the post title
and other information into the title, as well. (this behavior can be
overridden in the templates themselves)
"""
STATIC_TITLE = getattr(settings, 'EASYBLOG_STATIC_TTILE', 'Easy Blog')

"""
These keywords will show up in your HTML's keywords meta tag
if none are provided by the template. (this behavior can be
overridden in the templates themselves)
"""
DEFAULT_KEYWORDS = getattr(settings, 'EASYBLOG_DEFAULT_KEYWORDS', '')

"""
This description will show up i nyour HTML's description meta tag
if none are provided by the template. (this behavior can be
overridden in the templates themselves)
"""
DEFAULT_DESCRIPTION = getattr(settings, 'EASYBLOG_DEFAULT_DESCRIPTION', '')


"""
Defines the number of words in the auto generated post preview.
"""
POST_PREVIEW_WORD_COUNT = getattr(settings, 'EASYBLOG_POST_PREVIEW_WORD_COUNT', 500)

"""
Defines how many posts show per page
"""
POSTS_PER_PAGE = getattr(settings, 'EASYBLOG_POSTS_PER_PAGE', 10)

"""
"""
ALLOW_EMPTY = getattr(settings, 'EASYBLOG_ALLOW_EMPTY', True)

"""
"""
ALLOW_FUTURE = getattr(settings, 'EASYBLOG_ALLOW_FUTURE', True)

UPLOAD_DIR = getattr(settings, 'EASYBLOG_UPLOAD_DIR', '/tmp')
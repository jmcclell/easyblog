'''
Defines which post status is defaulted if none is selected in the Admin
console. Ensure that this ID exists. Out of the box, PostStatus with ID 1 is
the published status.
'''
DEFAULT_POST_STATUS_ID = 1

'''
Defines the number of posts to show per page on paginated pages such as index
and archive pages.
'''
POSTS_PER_PAGE = 3

'''
Defines the number of words in the auto generated post preview.
'''
POST_PREVIEW_WORD_COUNT = 500

'''
This title will always show up in your title as the first part. If you want
a separator, add it here. Templates will automatically insert the post title
and other information into the title, as well. (this behavior can be
overridden in the templates themselves)
'''
STATIC_TITLE = 'Easy Blog'

'''
These keywords will show up in your HTML's keywords meta tag
if none are provided by the template. (this behavior can be
overridden in the templates themselves)
'''
DEFAULT_KEYWORDS = ''

'''
This description will show up i nyour HTML's description meta tag
if none are provided by the template. (this behavior can be
overridden in the templates themselves)
'''
DEFAULT_DESCRIPTION = ''
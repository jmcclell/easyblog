from django.contrib import admin
from django.template.defaultfilters import slugify
from easyblog.models import Post, PostStatus, Category
    
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article', {'fields': ['title', 'slug', 'body', 'excerpt']}),
        ('Publishing', {'fields': ['status', 'publish_date']}), 
        ('Meta Data', {'fields': ['keywords', 'description']}),
        ('Series', {'fields': ['follows']})
    ]
    list_display = ('title', 'created_on', 'modified_on',
                    'publish_date', 'author', 'status', 'is_edited', 'is_live')
    list_filter = ['status', 'publish_date', 'author',
                   'created_on', 'modified_on']
    search_fields = ['title', 'body', 'keywords', 'description']
    date_hierarchy = 'publish_date'
    prepopulated_fields = {'slug': ['title']}
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            if not obj.slug:
                obj.slug = slugify(obj.title)
                
            if not obj.status:
                obj.status = PostStatus.live_statuses.get_default_status()
                
                
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


admin.site.register(PostStatus)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

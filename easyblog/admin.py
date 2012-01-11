from django.contrib import admin
from django.template.defaultfilters import slugify
from easyblog.models import Post, Tag, get_default_status
    
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article', {'fields': ['title', 'slug', 'body']}),
        ('Publishing', {'fields': ['status', 'publish_date']}),
        ('Tags', {'fields': ['tags']}),
        ('Meta Data', {'fields': ['keywords', 'description']}),
        ('Series', {'fields': ['follows']})
    ]
    list_display = ('title', 'created_on', 'modified_on',
                    'publish_date', 'user', 'status', 'is_edited', 'is_live')
    list_filter = ['status', 'publish_date', 'tags', 'user',
                   'created_on', 'modified_on']
    search_fields = ['title', 'body', 'tags', 'keywords', 'description']
    date_hierarchy = 'publish_date'
    prepopulated_fields = {'slug': ['title']}
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            if not obj.slug:
                obj.slug = slugify(obj.title)
                
            if not obj.status:
                obj.status = get_default_status()
                
                
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
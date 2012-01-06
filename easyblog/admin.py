from django.contrib import admin

from easyblog.models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article', {'fields': ['title', 'body']}),
        ('Publishing', {'fields': ['status', 'publish_date']}),
        ('Tags', {'fields': ['tags']}),
        ('Meta Data', {'fields': ['keywords', 'description']}),
        ('Related', {'fields': ['follows', 'related']})
    ]
    list_display = ('title', 'created_on', 'modified_on',
                    'publish_date', 'user', 'status', 'is_edited', 'is_live')
    list_filter = ['status', 'publish_date', 'tags', 'user',
                   'created_on', 'modified_on']
    search_fields = ['title', 'body', 'tags', 'keywords', 'description']
    date_hierarchy = 'publish_date'
        
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

from django.contrib import admin
from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status',)
    list_filter = ('status', 'publish')
    raw_id_fields = ('author', )
    search_fields = ('title', 'body',)
    ordering = ('status', 'publish', )
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}


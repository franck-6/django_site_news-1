# coding: utf8
from django.contrib.admin import ModelAdmin


class NewsItemAdmin(ModelAdmin):
    actions = None
    date_hierarchy = 'date'
    fields = ('section', 'date', 'title', 'snippet', 'body', 'site', 'picture', 'source_url', 'published', )
    list_display = ('site', 'section', 'date', 'title', 'snippet', 'published', )
    list_filter = ('section', 'published', 'site', )
    search_fields = ('name', )


class NewsItemSimplifiedAdmin(NewsItemAdmin):
    fields = ('section', 'date', 'site', 'snippet', 'body', 'published', )
    list_display = ('site', 'section', 'date', 'snippet', 'published', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.title = obj.snippet[:60]
        obj.save()

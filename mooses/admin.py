from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('title', 'get_image', 'category',)
    list_display_links = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="30">')
        return '-'

    get_image.short_description = 'Image'

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(About)

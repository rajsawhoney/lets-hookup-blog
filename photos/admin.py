from django.contrib import admin

from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    fields = ['file',]
    # readonly_fields = ['image_tag']
    list_display = ['file', 'image_tag', ]

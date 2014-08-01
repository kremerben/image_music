from django.contrib import admin
from models import *
# Register your models here.




class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'tag_list', 'download_url', )
    list_filter = ('genre',)


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Tag)


from django.contrib import admin
from .models import Music,Language,MovieAlbum

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ('movie_album_name','name', 'desc', 'date')

admin.site.register(Language)
admin.site.register(MovieAlbum)

admin.site.register(Music, MusicAdmin)
admin.site.site_header ="Music World"
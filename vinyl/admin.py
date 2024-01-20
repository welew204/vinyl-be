from django.contrib import admin
from .models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'bringer')

# Register your models here.

admin.site.register(Album, AlbumAdmin)
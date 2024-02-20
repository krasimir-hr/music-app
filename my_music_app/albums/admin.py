from django.contrib import admin

from my_music_app.albums.models import Album

@admin.register(Album)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'genre', 'owner')
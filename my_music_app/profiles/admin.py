from django.contrib import admin

from my_music_app.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')

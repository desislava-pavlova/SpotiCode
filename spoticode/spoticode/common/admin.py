# Django
from django.contrib import admin
# Project
from spoticode.common.models import MusicGroup, Genre
from spoticode.common.admin_filters import GenresFirstLetterFilter


# ----- Music Group Tables -----
@admin.register(MusicGroup)
class MusicGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name', 'songs_count', 'pending_count', 'description')
    search_fields = ('group_name',)
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count', 'pending_count']
        return []



# ----- Genres Tables -----
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name', 'songs_count', 'description')
    search_fields = ('genre_name', 'description')
    list_filter = (
        (GenresFirstLetterFilter),
    )
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count']
        return []

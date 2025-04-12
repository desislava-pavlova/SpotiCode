# Django
from django.contrib import admin
# Project
from spoticode.common.models import MusicGroup, Genre
from spoticode.common.admin_filters import GenresFirstLetterFilter


@admin.register(MusicGroup)
class MusicGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'songs_count', 'pending_count')
    search_fields = ('group_name',)
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count', 'pending_count']
        return []


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name', 'description', 'songs_count')
    search_fields = ('genre_name', 'description')
    list_filter = (
        (GenresFirstLetterFilter),
    )
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count']
        return []

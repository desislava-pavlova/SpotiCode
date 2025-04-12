# Django
from django.contrib import admin
# Project
from spoticode.songs.models import Song, PendingSong
from spoticode.songs.admin_filters import SongsAlbumsNoAlbumsFilter, SongsLinksNoLinksFilter
from spoticode.songs.admin_actions import make_added, copy_to_songs_table
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'artist', 'feat_artist', 'genre', 'song_year', 'group', 'album', 'spotify_link')
    search_fields = ('song_title', 'main_artist__artist_name', 'feat_artist', 'album_id__album_name')
    list_filter = (
        ('main_artist__artist_name', DropdownFilter),
        ('album_id__album_name', DropdownFilter),
        ('group_id__group_name', DropdownFilter),
        ('genre_id__genre_name', DropdownFilter),
        (SongsAlbumsNoAlbumsFilter), 
        (SongsLinksNoLinksFilter),
    )
    
    def artist(self, obj):
        return obj.main_artist.artist_name if obj.main_artist else None
    
    def genre(self, obj):
        return obj.genre_id.genre_name if obj.genre_id else '--unknown--'
    
    def group(self, obj):
        return obj.group_id.group_name if obj.group_id else None
    
    def album(self, obj):
        return obj.album_id.album_name if obj.album_id else '--single--'
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []


@admin.register(PendingSong)
class PendingSongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'main_artist', 'feat_artist', 'group', 'is_added', 'new_artist')
    search_fields = ('song_title', 'main_artist', 'feat_artist')
    list_filter = (
        ('to_group__group_name', DropdownFilter),
        ('is_added'),
        ('new_artist'),
    )
    
    actions = (make_added, copy_to_songs_table)
    
    def group(self, obj):
        return obj.to_group.group_name if obj.to_group else None
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'is_added', 'new_artist']
        return []

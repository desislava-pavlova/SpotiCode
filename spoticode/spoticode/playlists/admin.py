# Django
from django.contrib import admin
# Project
from spoticode.playlists.models import Playlist, SongPlaylistRelation
# Other 
from django_admin_listfilter_dropdown.filters import DropdownFilter


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('playlist_name', 'songs_count', 'spotify_count', 'playlist_link', 'notes')
    search_fields = ('playlist_name', 'notes')
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []


@admin.register(SongPlaylistRelation)
class SongPlaylistRelationAdmin(admin.ModelAdmin):
    list_display = ('playlist', 'song')
    search_fields = ('playlist_id__playlist_name', 'song_id__song_title',)
    list_filter = (
        ('playlist_id__playlist_name', DropdownFilter),
    )
    
    def playlist(self, obj):
        return obj.playlist_id.playlist_name if obj.playlist_id.playlist_name else ''
    
    def song(self, obj):
        return str(obj.song_id) if obj.song_id else ''
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []

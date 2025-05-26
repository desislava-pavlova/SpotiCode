# Django
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
# Project
from spoticode.albums.models import Album, AlbumLink
from spoticode.albums.admin_filters import AlbumsReleaseDateFilter, AlbumLinksFilter


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'release_date', 'artist', 'album_name', 'album_type', 'songs_album', 'songs_count')
    search_fields = ('album_artist__artist_name', 'album_artist__other_names', 'album_name')
    list_filter = (
        ('album_artist__artist_name', DropdownFilter),
        ('album_type', DropdownFilter),
        (AlbumsReleaseDateFilter),
    )
    
    def artist(self, obj):
        return obj.album_artist.artist_name if obj.album_artist else ''
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count']
        return []


@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    list_display = ('album', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('for_album__album_name', 'for_album__album_artist__artist_name')
    list_filter = (
        (AlbumLinksFilter),
    )
    
    def album(self, obj):
        return obj.for_album.album_name if obj.for_album else None

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)

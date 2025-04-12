# Django
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
# Project
from spoticode.albums.models import Album, AlbumLink
from spoticode.albums.admin_filters import AlbumsReleaseDateFilter, AlbumLinksFilter


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'release_date', 'artist', 'album_name', 'album_type')
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
            return ['id']
        return []


@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    list_display = ('album', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('id__album_name', 'id__album_artist__artist_name')
    list_filter = (
        (AlbumLinksFilter),
    )
    
    def album(self, obj):
        return obj.id.album_name if obj.id else None

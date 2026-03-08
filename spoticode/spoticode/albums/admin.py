# Django
from django.contrib import admin
from django.db.models import Q
# Project
from spoticode.albums.models import Album, AlbumLink, MissingDataAlbum, MissingDataAlbumLink
from spoticode.albums.admin_filters import AlbumsReleaseDateFilter, AlbumLinksFilter, MissingDataAlbumFilter, MissingDataAlbumLinkFilter
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


# ----- Original Tables -----
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'release_date', 'artist', 'album_name', 'album_type', 'songs_album', 'songs_count')
    search_fields = ('album_artist__artist_name', 'album_artist__other_names', 'album_name')
    list_filter = (
        ('album_artist__artist_name', DropdownFilter),
        (AlbumsReleaseDateFilter),
        ('album_type', DropdownFilter),
    )
    
    def artist(self, obj):
        return obj.album_artist.artist_name if obj.album_artist else ''
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count']
        return []


@admin.register(AlbumLink)
class AlbumLinkAdmin(admin.ModelAdmin):
    list_display = ('album', 'spotify_link', 'wikipedia_link', 'discogs_link', 'rateyourmusic_link')
    search_fields = ('for_album__album_name', 'for_album__album_artist__artist_name')
    list_filter = (
        ('for_album__album_artist__artist_name', DropdownFilter),
        (AlbumLinksFilter),
    )
    
    def album(self, obj):
        return f'"{obj.for_album.album_name}" by {obj.for_album.album_artist.artist_name}' if obj.for_album else None

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)



# ----- Missing Data Tables -----
@admin.register(MissingDataAlbum)
class MissingDataAlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'release_date', 'artist', 'album_name', 'album_type', 'songs_album', 'songs_count')
    search_fields = ('album_artist__artist_name', 'album_artist__other_names', 'album_name')
    list_filter = (
        ('album_artist__artist_name', DropdownFilter),
        (MissingDataAlbumFilter),
    )
    
    def artist(self, obj):
        return obj.album_artist.artist_name if obj.album_artist else ''
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(release_date__isnull=True) | Q(songs_album__isnull=True))
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'songs_count']
        return []


@admin.register(MissingDataAlbumLink)
class MissingDataAlbumLinkAdmin(admin.ModelAdmin):
    list_display = ('album', 'spotify_link', 'wikipedia_link', 'discogs_link', 'rateyourmusic_link')
    search_fields = ('for_album__album_name', 'for_album__album_artist__artist_name')
    list_filter = (
        ('for_album__album_artist__artist_name', DropdownFilter),
        (MissingDataAlbumLinkFilter),
    )
    
    def album(self, obj):
        return f'"{obj.for_album.album_name}" by {obj.for_album.album_artist.artist_name}' if obj.for_album else None
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(spotify_link__isnull=True) | Q(wikipedia_link__isnull=True) \
            | Q(rateyourmusic_link__isnull=True) | Q(discogs_link__isnull=True))

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)

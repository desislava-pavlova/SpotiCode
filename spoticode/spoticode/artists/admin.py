from django.contrib import admin
# Project
from spoticode.artists.models import Artist, ArtistLink
from spoticode.artists.admin_filters import ArtistsFirstLetterFilter, ArtistsFormedInFilter, ArtistLinksFilter


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name', 'other_names', 'year_formed', 'songs_count', 'albums_count')
    search_fields = ('artist_name', 'other_names')
    list_filter = (
        (ArtistsFormedInFilter),
        (ArtistsFirstLetterFilter),
    )
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['songs_count', 'albums_count']
        return []


@admin.register(ArtistLink)
class ArtistLinkAdmin(admin.ModelAdmin):
    list_display = ('artist', 'official_website', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('id__artist_name', 'id__other_names')
    list_filter = (
        (ArtistLinksFilter),
        (ArtistsFirstLetterFilter), 
    )
    
    def artist(self, obj):
        return obj.id.artist_name if obj.id else ''

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)

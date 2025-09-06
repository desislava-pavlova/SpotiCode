from django.contrib import admin
from django.db.models import Q
# Project
from spoticode.artists.models import Artist, ArtistLink, MissingDataArtist, MissingDataArtistLink
from spoticode.artists.admin_filters import ArtistsFirstLetterFilter, ArtistsFormedInFilter, ArtistLinksFilter, MissingDataArtistFilter, MissingDataArtistLinkFilter
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


# Original Tables
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name', 'other_names', 'year_formed', 'origin', 'songs_count', 'albums_count')
    search_fields = ('artist_name', 'other_names')
    list_filter = (
        (ArtistsFormedInFilter),
        ('origin', DropdownFilter),
        (ArtistsFirstLetterFilter),
    )
    
    def get_exclude(self, request, obj=None):
        return ['songs_count', 'albums_count']


@admin.register(ArtistLink)
class ArtistLinkAdmin(admin.ModelAdmin):
    list_display = ('artist', 'official_website', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('for_artist__artist_name', 'for_artist__other_names')
    list_filter = (
        (ArtistLinksFilter),
        (ArtistsFirstLetterFilter), 
    )
    
    def artist(self, obj):
        return obj.for_artist.artist_name if obj.for_artist else ''

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)



# Missing Data Tables
@admin.register(MissingDataArtist)
class MissingDataArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name', 'other_names', 'year_formed', 'origin', 'songs_count', 'albums_count')
    search_fields = ('artist_name', 'other_names')
    list_filter = (
        (MissingDataArtistFilter),
        (ArtistsFirstLetterFilter),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(year_formed__isnull=True) | Q(origin__isnull=True) | ~Q(origin__contains=','))
    
    def get_exclude(self, request, obj=None):
        return ['songs_count', 'albums_count']


@admin.register(MissingDataArtistLink)
class MissingDataArtistLinkAdmin(admin.ModelAdmin):
    list_display = ('artist', 'official_website', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('for_artist__artist_name', 'for_artist__other_names')
    list_filter = (
        (MissingDataArtistLinkFilter),
        (ArtistsFirstLetterFilter), 
    )
    
    def artist(self, obj):
        return obj.for_artist.artist_name if obj.for_artist else ''
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(official_website__isnull=True) | Q(spotify_link__isnull=True) \
            | Q(wikipedia_link__isnull=True) | Q(rateyourmusic_link__isnull=True))

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        super().save_model(request, obj, form, change)

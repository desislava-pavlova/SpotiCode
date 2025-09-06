from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class SongsAlbumsNoAlbumsFilter(admin.SimpleListFilter):
    title = _('Album Relations')
    parameter_name = 'album_relations'

    def lookups(self, request, model_admin):
        return (
            ('Singles', _('Singles')),
            ('Album-Related', _('Album-Related')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Singles':
            return queryset.filter(album_id__isnull=True)
        elif self.value() == 'Album-Related':
            return queryset.filter(album_id__isnull=False)


class SongsLinksNoLinksFilter(admin.SimpleListFilter):
    title = _('Links')
    parameter_name = 'links'
    
    def lookups(self, request, model_admin):
        return (
            ('youtube_video', _('YouTube Video')),
            ('no_youtube_video', _('No YouTube Video')),
            ('youtube_audio', _('YouTube Audio')),
            ('no_youtube_audio', _('No YouTube Audio')),
            ('spotify', _('Spotify')),
            ('no_spotify', _('No Spotify')),
            ('wikipedia', _('Wikipedia')),
            ('no_wikipedia', _('No Wikipedia')),
            ('rateyourmusic', _('RateYourMusic')),
            ('no_rateyourmusic', _('No RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'youtube_video':
            return queryset.filter(youtube_video_link__isnull=False)
        elif self.value() == 'no_youtube_video':
            return queryset.filter(youtube_video_link__isnull=True)
        elif self.value() == 'youtube_audio':
            return queryset.filter(youtube_audio_link__isnull=False)
        elif self.value() == 'no_youtube_audio':
            return queryset.filter(youtube_audio_link__isnull=True)
        elif self.value() == 'spotify':
            return queryset.filter(spotify_link__isnull=False)
        elif self.value() == 'no_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'wikipedia':
            return queryset.filter(wikipedia_link__isnull=False)
        elif self.value() == 'no_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=False)
        elif self.value() == 'no_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)


class MissingDataSongFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_song_year', _('Missing Release Year')),
            ('missing_genre', _('Missing Genre')),
            ('missing_album', _('Missing Album')),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_song_year':
            return queryset.filter(song_year__isnull=True)
        elif self.value() == 'missing_genre':
            return queryset.filter(genre_id__isnull=True)
        elif self.value() == 'missing_album':
            return queryset.filter(album_id__isnull=True)


class MissingDataSongLinkFilter(admin.SimpleListFilter):
    title = _('Links')
    parameter_name = 'links'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_youtube_video', _('Missing YouTube Video')),
            ('missing_youtube_audio', _('Missing YouTube Audio')),
            ('missing_spotify', _('Missing Spotify')),
            ('missing_wikipedia', _('Missing Wikipedia')),
            ('missing_rateyourmusic', _('Missing RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_youtube_video':
            return queryset.filter(youtube_video_link__isnull=True)
        elif self.value() == 'missing_youtube_audio':
            return queryset.filter(youtube_audio_link__isnull=True)
        elif self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

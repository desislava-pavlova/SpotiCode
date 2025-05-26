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
            return queryset.filter(rateroumusic_link__is_null=False)
        elif self.value() == 'no_rateyourmusic':
            return queryset.filter(rateroumusic_link__is_null=True)

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Other 
from django_admin_listfilter_dropdown.filters import SimpleDropdownFilter


# ----- Pending Song Filters -----
class PendingSongAddedFilter(SimpleDropdownFilter):
    title = _('Added')
    parameter_name = 'added'

    def lookups(self, request, model_admin):
        return (
            ('Yes', _('Yes')),
            ('No', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(is_added=True)
        elif self.value() == 'No':
            return queryset.filter(is_added=False)


class PendingSongNewArtistFilter(SimpleDropdownFilter):
    title = _('New Artist')
    parameter_name = 'is_new_artist'

    def lookups(self, request, model_admin):
        return (
            ('Yes', _('Yes')),
            ('No', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(new_artist=True)
        elif self.value() == 'No':
            return queryset.filter(new_artist=False)



# ----- Song Filters -----
class SongsAlbumsNoAlbumsFilter(SimpleDropdownFilter):
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



# ----- Songs Link Filters -----
class SongsLinksNoLinksFilter(SimpleDropdownFilter):
    title = _('Links')
    parameter_name = 'links'
    
    def lookups(self, request, model_admin):
        return (
            ('file_path', _('File Path - YES')),
            ('no_file_path', _('File Path - NO')),
            ('youtube_video', _('YouTube Video - YES')),
            ('no_youtube_video', _('YouTube Video - NO')),
            ('youtube_audio', _('YouTube Audio - YES')),
            ('no_youtube_audio', _('YouTube Audio - NO')),
            ('spotify', _('Spotify - YES')),
            ('no_spotify', _('Spotify - NO')),
            ('wikipedia', _('Wikipedia - YES')),
            ('no_wikipedia', _('Wikipedia - NO')),
            ('rateyourmusic', _('RateYourMusic - YES')),
            ('no_rateyourmusic', _('RateYourMusic - NO')),
        )
        
    def queryset(self, request, queryset):
        if self.value() == 'file_path':
            return queryset.filter(file_path__isnull=False)
        elif self.value() == 'no_file_path':
            return queryset.filter(file_path__isnull=True)
        elif self.value() == 'youtube_video':
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



# ----- Missing Data - Song Filters -----
class MissingDataSongFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_song_year', _('Release Year')),
            ('missing_duration', _('Duration')),
            ('missing_genre', _('Genre')),
            ('missing_album', _('Album')),
            ('missing_notes', _('Notes')),            
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_song_year':
            return queryset.filter(song_year__isnull=True)
        elif self.value() == 'missing_duration':
            return queryset.filter(duration__isnull=True)
        elif self.value() == 'missing_genre':
            return queryset.filter(genre_id__isnull=True)
        elif self.value() == 'missing_album':
            return queryset.filter(album_id__isnull=True)
        elif self.value() == 'missing_notes':
            return queryset.filter(notes__isnull=True)


class MissingDataSongLinkFilter(admin.SimpleListFilter):
    title = _('Missing Links')
    parameter_name = 'missing_links'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_file_path', _('File Path')),
            ('missing_youtube_video', _('YouTube Video')),
            ('missing_youtube_audio', _('YouTube Audio')),
            ('missing_spotify', _('Spotify')),
            ('missing_wikipedia', _('Wikipedia')),
            ('missing_rateyourmusic', _('RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_file_path':
            return queryset.filter(file_path__isnull=True)
        elif self.value() == 'missing_youtube_video':
            return queryset.filter(youtube_video_link__isnull=True)
        elif self.value() == 'missing_youtube_audio':
            return queryset.filter(youtube_audio_link__isnull=True)
        elif self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

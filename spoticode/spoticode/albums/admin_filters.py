from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AlbumsReleaseDateFilter(admin.SimpleListFilter):
    title = _('Release Date')
    parameter_name = 'release_date'

    def lookups(self, request, model_admin):
        return (
            ('1900-1989', _('1900-1989')),
            ('1990-1999', _('1990-1999')),
            ('2000-2010', _('2000-2010')),
            ('2011-2020', _('2011-2020')),
            ('2021-2030', _('2021-2030')),
            ('none', _('None')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1900-1989':
            return queryset.filter(release_date__range=['1900-01-01', '1989-12-31'])
        elif self.value() == '1990-1999':
            return queryset.filter(release_date__range=['1990-01-01', '1999-12-31'])
        elif self.value() == '2000-2010':
            return queryset.filter(release_date__range=['2000-01-01', '2010-12-31'])
        elif self.value() == '2011-2020':
            return queryset.filter(release_date__range=['2011-01-01', '2020-12-31'])
        elif self.value() == '2021-2030':
            return queryset.filter(release_date__range=['2021-01-01', '2030-12-31'])
        elif self.value() == 'none':
            return queryset.filter(release_date__isnull=True)


class AlbumLinksFilter(admin.SimpleListFilter):
    title = _('Links')
    parameter_name = 'links'

    def lookups(self, request, model_admin):
        return (
            ('spotify', _('Spotify')),
            ('no_spotify', _('No Spotify')),
            ('wikipedia', _('Wikipedia')),
            ('no_wikipedia', _('No Wikipedia')),
            ('rateyourmusic', _('RateYourMusic')),
            ('no_rateyourmusic', _('No RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'spotify':
            return queryset.filter(spotify_link__isnull=False)
        elif self.value() == 'no_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'wikipedia':
            return queryset.filter(wikipedia_link__isnull=False)
        elif self.value() == 'no_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'rateyourmusic':
            return queryset.filter(raterourmusic_link__isnull=False)
        elif self.value() == 'no_rateyourmusic':
            return queryset.filter(raterourmusic_link__isnull=True)


class MissingDataAlbumFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_release_date', _('Missing Release Date')),
            ('missing_total_songs', _('Missing Total Songs')),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_release_date':
            return queryset.filter(release_date__isnull=True)
        elif self.value() == 'missing_total_songs':
            return queryset.filter(songs_album__isnull=True)


class MissingDataAlbumLinkFilter(admin.SimpleListFilter):
    title = _('Missing Links')
    parameter_name = 'missing_links'

    def lookups(self, request, model_admin):
        return (
            ('missing_spotify', _('Missing Spotify')),
            ('missing_wikipedia', _('Missing Wikipedia')),
            ('missing_rateyourmusic', _('Missing RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

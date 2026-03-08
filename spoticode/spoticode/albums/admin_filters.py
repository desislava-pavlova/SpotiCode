from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Other 
from django_admin_listfilter_dropdown.filters import SimpleDropdownFilter


# ----- Album Filters -----
class AlbumsReleaseDateFilter(SimpleDropdownFilter):
    title = _('Release Date')
    parameter_name = 'release_date'

    def lookups(self, request, model_admin):
        return (
            ('-', _('-')),
            ('1900-1989', _('1900-1989')),
            ('1990-1999', _('1990-1999')),
            ('2000-2010', _('2000-2010')),
            ('2011-2020', _('2011-2020')),
            ('2021-2030', _('2021-2030')),
        )

    def queryset(self, request, queryset):
        if self.value() == '-':
            return queryset.filter(release_date__isnull=True)
        elif self.value() == '1900-1989':
            return queryset.filter(release_date__range=['1900-01-01', '1989-12-31'])
        elif self.value() == '1990-1999':
            return queryset.filter(release_date__range=['1990-01-01', '1999-12-31'])
        elif self.value() == '2000-2010':
            return queryset.filter(release_date__range=['2000-01-01', '2010-12-31'])
        elif self.value() == '2011-2020':
            return queryset.filter(release_date__range=['2011-01-01', '2020-12-31'])
        elif self.value() == '2021-2030':
            return queryset.filter(release_date__range=['2021-01-01', '2030-12-31'])



# ----- Album Links Filters -----
class AlbumLinksFilter(SimpleDropdownFilter):
    title = _('Links')
    parameter_name = 'links'

    def lookups(self, request, model_admin):
        return (
            ('spotify', _('Spotify - YES')),
            ('no_spotify', _('Spotify - NO')),
            ('wikipedia', _('Wikipedia - YES')),
            ('no_wikipedia', _('Wikipedia - NO')),
            ('discogs', _('Discogs - YES')),
            ('no_discogs', _('Discogs - NO')),
            ('rateyourmusic', _('RateYourMusic - YES')),
            ('no_rateyourmusic', _('RateYourMusic - NO')),
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
        elif self.value() == 'discogs':
            return queryset.filter(discogs_link__isnull=False)
        elif self.value() == 'no_discogs':
            return queryset.filter(discogs_link__isnull=True)
        elif self.value() == 'rateyourmusic':
            return queryset.filter(raterourmusic_link__isnull=False)
        elif self.value() == 'no_rateyourmusic':
            return queryset.filter(raterourmusic_link__isnull=True)



# ----- Missing Data - Artist Filters -----
class MissingDataAlbumFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_release_date', _('Release Date')),
            ('missing_total_songs', _('Total Songs')),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_release_date':
            return queryset.filter(release_date__isnull=True)
        elif self.value() == 'missing_total_songs':
            return queryset.filter(songs_album__isnull=True)



# ----- Missing Data - Artist Links Filters -----
class MissingDataAlbumLinkFilter(admin.SimpleListFilter):
    title = _('Missing Links')
    parameter_name = 'missing_links'

    def lookups(self, request, model_admin):
        return (
            ('missing_spotify', _('Spotify')),
            ('missing_wikipedia', _('Wikipedia')),
            ('missing_discogs', _('Discogs')),
            ('missing_rateyourmusic', _('RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_discogs':
            return queryset.filter(discogs_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

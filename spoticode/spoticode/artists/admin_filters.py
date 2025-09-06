from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Project
from spoticode.artists.models import Artist


class ArtistsFirstLetterFilter(admin.SimpleListFilter):
    title = _('First Letter')
    parameter_name = 'artist_name_letter'
    
    def lookups(self, request, model_admin):
        all_artist_names = Artist.objects.values_list('artist_name', flat=True)
        first_letters = sorted(set(name[0].upper() for name in all_artist_names if name))
        return tuple((letter, letter) for letter in first_letters)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(artist_name__istartswith=self.value())
        return queryset


class ArtistsFormedInFilter(admin.SimpleListFilter):
    title = _('Formed In')
    parameter_name = 'year_formed'

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


class ArtistLinksFilter(admin.SimpleListFilter):
    title = _('Links')
    parameter_name = 'links'
    
    def lookups(self, request, model_admin):
        return (
            ('official_website', _('Official Website')),
            ('no_official_website', _('No Official Website')),
            ('spotify', _('Spotify')),
            ('no_spotify', _('No Spotify')),
            ('wikipedia', _('Wikipedia')),
            ('no_wikipedia', _('No Wikipedia')),
            ('rateyourmusic', _('RateYourMusic')),
            ('no_rateyourmusic', _('No RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'official_website':
            return queryset.filter(official_website__isnull=False)
        elif self.value() == 'no_official_website':
            return queryset.filter(official_website__isnull=True)
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


class MissingDataArtistFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_year_formed', _('Missing Formed In')),
            ('missing_origin', _('Missing Origin')),
            ('missing_origin_city', _('Missing Origin City'))
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_year_formed':
            return queryset.filter(year_formed__isnull=True),
        elif self.value() == 'missing_origin':
            return queryset.filter(origin__isnull=True)
        elif self.value() == 'missing_origin_city':
            return queryset.exclude(origin__contains=',').filter(origin__isnull=False)


class MissingDataArtistLinkFilter(admin.SimpleListFilter):
    title = _('Missing Links')
    parameter_name = 'missing_links'

    def lookups(self, request, model_admin):
        return (
            ('missing_official_website', _('Missing Official Website')),
            ('missing_spotify', _('Missing Spotify')),
            ('missing_wikipedia', _('Missing Wikipedia')),
            ('missing_rateyourmusic', _('Missing RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_official_website':
            return queryset.filter(official_website__isnull=True)
        elif self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

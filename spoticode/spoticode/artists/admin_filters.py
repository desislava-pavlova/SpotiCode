from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Project
from spoticode.artists.models import Artist, ArtistLink
# Other 
from django_admin_listfilter_dropdown.filters import SimpleDropdownFilter


# ----- Artist Filters -----
class ArtistsFirstLetterFilter(SimpleDropdownFilter):
    title = _('First Letter')
    parameter_name = 'artist_name_letter'
    
    def lookups(self, request, model_admin):
        all_artist_names = Artist.objects.values_list('artist_name', flat=True)
        
        numeric_found = False
        letters = set() 
        
        for name in all_artist_names:
            if not name:
                continue
            
            first = name[0].upper()
            
            if first.isdigit():
                numeric_found = True 
            else:
                letters.add(first)
        
        lookup_list = []
        if numeric_found:
            lookup_list.append(('0-9', '0-9'))
        
        for letter in sorted(letters):
            lookup_list.append((letter, letter))
        
        return tuple(lookup_list)
        

    def queryset(self, request, queryset):
        if self.value() == '0-9':
            return queryset.filter(artist_name__regex=r"^[0-9]")
        elif self.value():
            return queryset.filter(artist_name__istartswith=self.value())
        return queryset


class ArtistsFormedInFilter(SimpleDropdownFilter):
    title = _('Formed In')
    parameter_name = 'year_formed'

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


class ArtistOriginFilter(SimpleDropdownFilter):
    title = _('Origin')
    parameter_name = 'filtered_origin'

    def lookups(self, request, model_admin):
        origins = Artist.objects.values_list('origin', flat=True)
        values = set()

        for origin in origins:
            if not origin:
                continue

            parts = [p.strip() for p in origin.split(",")]

            if parts[-1].upper() == "USA":
                values.add(parts[-2] + ", USA")
            else:
                values.add(parts[-1])

        sorted_values = sorted(values, key=lambda v: (v.endswith(", USA"), v))
        sorted_values.insert(0, "__no_origin__")

        return [(v, "-" if v == "__no_origin__" else v) for v in sorted_values]

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == "__no_origin__":
                return queryset.filter(origin__isnull=True)
            return queryset.filter(origin__iendswith=self.value())
        return queryset



# ----- Artist Links Filters -----
class ArtistsLinksFirstLetterFilter(SimpleDropdownFilter):
    title = _('Artist First Letter')
    parameter_name = 'artist_name_letter'
    
    def lookups(self, request, model_admin):
        all_artist_names = ArtistLink.objects.values_list('for_artist__artist_name', flat=True)
        
        numeric_found = False
        letters = set() 
        
        for name in all_artist_names:
            if not name:
                continue
            
            first = name[0].upper()
            
            if first.isdigit():
                numeric_found = True 
            else:
                letters.add(first)
        
        lookup_list = []
        if numeric_found:
            lookup_list.append(('0-9', '0-9'))
        
        for letter in sorted(letters):
            lookup_list.append((letter, letter))
        
        return tuple(lookup_list)
        

    def queryset(self, request, queryset):
        if self.value() == '0-9':
            return queryset.filter(for_artist__artist_name__regex=r"^[0-9]")
        elif self.value():
            return queryset.filter(for_artist__artist_name__istartswith=self.value())
        return queryset


class ArtistLinksFilter(SimpleDropdownFilter):
    title = _('Links')
    parameter_name = 'links'
    
    def lookups(self, request, model_admin):
        return (
            ('official_website', _('Official Website - YES')),
            ('no_official_website', _('Official Website - NO')),
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
        elif self.value() == 'discogs':
            return queryset.filter(discogs_link__isnull=False)
        elif self.value() == 'no_discogs':
            return queryset.filter(discogs_link__isnull=True)
        elif self.value() == 'rateyourmusic':
            return queryset.filter(rateroumusic_link__is_null=False)
        elif self.value() == 'no_rateyourmusic':
            return queryset.filter(rateroumusic_link__is_null=True)



# ----- Missing Data - Artist Filters -----
class MissingDataArtistFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_year_formed', _('Formed In')),
            ('missing_origin', _('Origin')),
            ('missing_origin_city', _('Origin City'))
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_year_formed':
            return queryset.filter(year_formed__isnull=True),
        elif self.value() == 'missing_origin':
            return queryset.filter(origin__isnull=True)
        elif self.value() == 'missing_origin_city':
            return queryset.exclude(origin__contains=',').filter(origin__isnull=False)



# ----- Missing Data - Artist Links Filters -----
class MissingDataArtistLinkFilter(admin.SimpleListFilter):
    title = _('Missing Links')
    parameter_name = 'missing_links'

    def lookups(self, request, model_admin):
        return (
            ('missing_official_website', _('Official Website')),
            ('missing_spotify', _('Spotify')),
            ('missing_wikipedia', _('Wikipedia')),
            ('missing_discogs', _('Discogs')),
            ('missing_rateyourmusic', _('RateYourMusic')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'missing_official_website':
            return queryset.filter(official_website__isnull=True)
        elif self.value() == 'missing_spotify':
            return queryset.filter(spotify_link__isnull=True)
        elif self.value() == 'missing_wikipedia':
            return queryset.filter(wikipedia_link__isnull=True)
        elif self.value() == 'missing_discogs':
            return queryset.filter(discogs_link__isnull=True)
        elif self.value() == 'missing_rateyourmusic':
            return queryset.filter(rateyourmusic_link__isnull=True)

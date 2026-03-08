# Django
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# ----- Missing Data - Playlist Filters -----
class MissingDataPlaylistFilter(admin.SimpleListFilter):
    title = _('Missing Data')
    parameter_name = 'missing_data'
    
    def lookups(self, request, model_admin):
        return (
            ('missing_playlist_link', _('Playlist Link')),
            ('missing_notes', _('Notes')),            
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'missing_playlist_link':
            return queryset.filter(playlist_link__isnull=True)
        elif self.value() == 'missing_notes':
            return queryset.filter(notes__isnull=True)

# Django
from django.contrib import admin
from django.db.models import Q
# Project
from spoticode.songs.models import Song, SongLink, PendingSong, MissingDataSong, MissingDataSongLink
from spoticode.songs.admin_filters import PendingSongAddedFilter, PendingSongNewArtistFilter
from spoticode.songs.admin_filters import SongsAlbumsNoAlbumsFilter, SongsLinksNoLinksFilter
from spoticode.songs.admin_filters import MissingDataSongFilter, MissingDataSongLinkFilter
from spoticode.songs.admin_actions import make_added, copy_to_songs_table
# Other
from django_admin_listfilter_dropdown.filters import DropdownFilter


# ----- Pending Songs Tables -----
@admin.register(PendingSong)
class PendingSongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'main_artist', 'feat_artist', 'group', 'is_added', 'new_artist')
    search_fields = ('song_title', 'main_artist', 'feat_artist')
    list_filter = (
        ('to_group__group_name', DropdownFilter),
        (PendingSongAddedFilter),
        (PendingSongNewArtistFilter),
    )
    
    actions = (make_added, copy_to_songs_table)
    
    def group(self, obj):
        return obj.to_group.group_name if obj.to_group else None
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id', 'is_added', 'new_artist']
        return []



# ----- Original Song Tables -----
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'artist', 'feat_artist', 'genre', 'song_year', 'duration', 'group', 'album', 'notes')
    search_fields = ('song_title', 'main_artist__artist_name', 'feat_artist', 'album_id__album_name')
    list_filter = (
        ('main_artist__artist_name', DropdownFilter),
        ('album_id__album_name', DropdownFilter),
        ('group_id__group_name', DropdownFilter),
        ('genre_id__genre_name', DropdownFilter),
        (SongsAlbumsNoAlbumsFilter),
    )
    
    def artist(self, obj):
        return obj.main_artist.artist_name if obj.main_artist else None
    
    def genre(self, obj):
        return obj.genre_id.genre_name if obj.genre_id else '--unknown--'
    
    def group(self, obj):
        return obj.group_id.group_name if obj.group_id else None
    
    def album(self, obj):
        return obj.album_id.album_name if obj.album_id else '--single--'
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []


@admin.register(SongLink)
class SongLinkAdmin(admin.ModelAdmin):
    list_display = ('song', 'file_path', 'youtube_video_link', 'youtube_audio_link', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('for_song__song_title', 'for_song__main_artist__artist_name')
    list_filter = (
        ('for_song__main_artist__artist_name', DropdownFilter),
        (SongsLinksNoLinksFilter), 
    )
    
    def song(self, obj):
        return obj.for_song if obj.for_song else '--error--'

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        if obj.youtube_video_link and '&list=' in obj.youtube_video_link:
            obj.youtube_video_link = obj.youtube_video_link.split('&list=')[0]
        if obj.youtube_audio_link and '&list=' in obj.youtube_audio_link:
            obj.youtube_audio_link = obj.youtube_audio_link.split('&list=')[0]
        super().save_model(request, obj, form, change)



# ----- Missing Data Song Tables -----
@admin.register(MissingDataSong)
class MissingDataSongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'artist', 'feat_artist', 'genre', 'song_year','duration', 'group', 'album', 'notes')
    search_fields = ('song_title', 'main_artist__artist_name', 'feat_artist', 'album_id__album_name')
    list_filter = (
        ('main_artist__artist_name', DropdownFilter),
        ('group_id__group_name', DropdownFilter),
        (MissingDataSongFilter),
    )
    
    def artist(self, obj):
        return obj.main_artist.artist_name if obj.main_artist else None
    
    def genre(self, obj):
        return obj.genre_id.genre_name if obj.genre_id else None
    
    def group(self, obj):
        return obj.group_id.group_name if obj.group_id else None
    
    def album(self, obj):
        return obj.album_id.album_name if obj.album_id else None
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(song_year__isnull=True) | Q(genre_id__isnull=True) | Q(album_id__isnull=True) | Q(duration__isnull=True))
    
    def get_exclude(self, request, obj=None):
        if obj is None:
            return ['id',]
        return []


@admin.register(MissingDataSongLink)
class MissingDataSongLinkAdmin(admin.ModelAdmin):
    list_display = ('song', 'file_path', 'youtube_video_link', 'youtube_audio_link', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link')
    search_fields = ('for_song__song_title', 'for_song__main_artist__artist_name')
    list_filter = (
        ('for_song__main_artist__artist_name', DropdownFilter),
        (MissingDataSongLinkFilter), 
    )
    
    def song(self, obj):
        return obj.for_song if obj.for_song else '--error--'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(Q(youtube_video_link__isnull=True) | Q(youtube_audio_link__isnull=True) | Q(spotify_link__isnull=True) \
            | Q(wikipedia_link__isnull=True) | Q(rateyourmusic_link__isnull=True))

    def save_model(self, request, obj, form, change):
        if obj.spotify_link and '?si=' in obj.spotify_link:
            obj.spotify_link = obj.spotify_link.split('?si=')[0]
        if obj.youtube_video_link and '&list=' in obj.youtube_video_link:
            obj.youtube_video_link = obj.youtube_video_link.split('&list=')[0]
        if obj.youtube_audio_link and '&list=' in obj.youtube_audio_link:
            obj.youtube_audio_link = obj.youtube_audio_link.split('&list=')[0]
        super().save_model(request, obj, form, change)

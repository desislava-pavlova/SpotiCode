import uuid
from datetime import datetime
# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Project
from spoticode.common.models import MusicGroup


class Song(models.Model):
    YEAR_MIN_VALUE = 1860
    YEAR_MAX_VALUE = datetime.now().year
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    song_title = models.CharField(db_column='song_title', verbose_name='Title')
    main_artist = models.ForeignKey(to='artists.Artist', to_field='id', on_delete=models.RESTRICT, 
                                    db_column='main_artist', verbose_name='Artist')
    feat_artist = models.CharField(null=True, blank=True, 
                                   db_column='feat_artist', verbose_name='feat. Artists')
    song_year = models.IntegerField(null=True, blank=True, 
                                    validators=[MinValueValidator(YEAR_MIN_VALUE, 'First recording is in 1860. Have you found new history?'), 
                                                MaxValueValidator(YEAR_MAX_VALUE, 'Woah, are you coming from the future?')], 
                                    db_column='song_year', verbose_name='Release Year')
    genre_id = models.ForeignKey(to='common.Genre', to_field='id', on_delete=models.SET_NULL, 
                              null=True, blank=True, 
                              db_column='genre_id', verbose_name='Genre')
    album_id = models.ForeignKey(to='albums.Album', to_field='id', on_delete=models.SET_NULL, 
                                 null=True, blank=True, 
                                 db_column='album_id', verbose_name='Album')
    group_id = models.ForeignKey(to='common.MusicGroup', to_field='id', on_delete=models.SET_DEFAULT, 
                              blank=True, default=MusicGroup.get_default_group, 
                              db_column='group_id', verbose_name='Group')
    notes = models.TextField(null=True, blank=True, 
                             db_column='notes', verbose_name='Notes')

    def __str__(self):
        if self.feat_artist is not None:
            return f'{self.main_artist.artist_name} - {self.song_title} (feat. {self.feat_artist})'
        else:
            return f'{self.main_artist.artist_name} - {self.song_title}'
    
    @classmethod
    def field_order(cls):
        return ['song_year', 'genre_id', 'album_id', 'group_id', 'notes', 'id']
    
    def save(self, *args, **kwargs):
        if not self.notes:
            self.notes = None
        
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'songs'
        unique_together = (('song_title', 'main_artist'),)
        ordering = ('main_artist', 'song_title')
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'


class SongLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    for_song = models.OneToOneField(Song, to_field='id', on_delete=models.CASCADE, 
                              db_column='for_song', verbose_name='For Song')
    file_path = models.CharField(null=True, blank=True, unique=True, 
                                       db_column='file_path', verbose_name='File Path')
    youtube_video_link = models.URLField(null=True, blank=True, unique=True, 
                                       db_column='youtube_video_link', verbose_name='YouTube Video Link')
    youtube_audio_link = models.URLField(null=True, blank=True, unique=True, 
                                       db_column='youtube_audio_link', verbose_name='YouTube Audio Link')
    spotify_link = models.URLField(null=True, blank=True, unique=True, 
                                   db_column='spotify_link', verbose_name='Spotify Link')
    wikipedia_link = models.URLField(null=True, blank=True, unique=True, 
                                     db_column='wikipedia_link', verbose_name='Wikipedia Link')
    rateyourmusic_link = models.URLField(null=True, blank=True, unique=True, 
                                         db_column='rateyourmusic_link', verbose_name='Rate Your Music Link')

    def __str__(self):
        return f'Links for song: {self.id}'
    
    @classmethod
    def field_order(cls):
        return ['file_path', 'youtube_video_link', 'youtube_audio_link', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link']
    
    class Meta:
        db_table = 'songs_links'
        ordering = ('for_song__main_artist__artist_name', 'for_song__song_title')
        verbose_name = 'Songs Link'
        verbose_name_plural = 'Songs Links'


class PendingSong(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    song_title = models.CharField(db_column='song_title', verbose_name='Title')
    main_artist = models.CharField(db_column='main_artist', verbose_name='Artist')
    feat_artist = models.CharField(null=True, blank=True, 
                                   db_column='feat_artist', verbose_name='Feat. Artist')
    to_group = models.ForeignKey(to='common.MusicGroup', to_field='id', on_delete=models.SET_DEFAULT, 
                                 blank=True, default=MusicGroup.get_default_group, 
                                 db_column='to_group', verbose_name='Group')
    is_added = models.BooleanField(blank=True, default=False, 
                                   db_column='is_added', verbose_name='Added')
    new_artist = models.BooleanField(blank=True, default=False, 
                                     db_column='new_artist', verbose_name='New Artist')
    
    def __str__(self):
        if self.feat_artist is not None:
            return f'{self.main_artist} - {self.song_title} (feat. {self.feat_artist})'
        else:
            return f'{self.main_artist} - {self.song_title}'
    
    @classmethod
    def field_order(cls):
        return ['to_group', 'is_added', 'new_artist', 'id']
    
    class Meta:
        db_table = 'pending_songs'
        unique_together = (('song_title', 'main_artist'),)
        ordering = ('main_artist', 'song_title')
        verbose_name = 'Pending Song'
        verbose_name_plural = 'Pending Songs'



# Missing data models
class MissingDataSong(Song):
    class Meta:
        proxy = True
        verbose_name = "Z_Missing Data: Songs"
        verbose_name_plural = "Z_Missing Data: Songs"


class MissingDataSongLink(SongLink):
    class Meta:
        proxy = True
        verbose_name = "Z_Missing Data: Songs Links"
        verbose_name_plural = "Z_Missing Data: Songs Links"

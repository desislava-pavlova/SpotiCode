import uuid
# Django
from django.db import models


class Playlist(models.Model):
    COUNTER_DEFAULT = 0
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    playlist_name = models.CharField(unique=True, 
                                     db_column='playlist_name', verbose_name='Playlist Name')
    songs_count = models.PositiveIntegerField(blank=True, default=COUNTER_DEFAULT, 
                                              db_column='songs_count', verbose_name='Total Songs')
    spotify_count = models.PositiveIntegerField(blank=True, default=COUNTER_DEFAULT, 
                                                db_column='spotify_count', verbose_name='Total Songs on Spotify')
    playlist_link = models.URLField(null=True, blank=True, unique=True, 
                                    db_column='playlist_link', verbose_name='Playlist Link')
    playlist_image = models.ImageField(null=True, blank=True, 
                                       db_column='playlist_image', verbose_name='Image')
    notes = models.TextField(null=True, blank=True, 
                             db_column='notes', verbose_name='Notes')
    
    def __str__(self):
        return f'Playlist: "{self.playlist_name}"'
    
    class Meta:
        db_table = 'playlists'
        ordering = ('playlist_name',)
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'


class SongPlaylistRelation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    playlist_id = models.ForeignKey(to='playlists.Playlist', to_field='id', on_delete=models.CASCADE, 
                                    db_column='playlist_id', verbose_name='Playlist ID')
    song_id = models.ForeignKey(to='songs.Song', to_field='id', on_delete=models.CASCADE, 
                                db_column='song_id', verbose_name='Song ID')
    
    def __str__(self):
        return f'Relation for {self.playlist_id.playlist_name} - "{str(self.song_id)}"'
    
    class Meta:
        db_table = 'song_playlist_relations'
        unique_together = (('playlist_id', 'song_id'),)
        verbose_name = 'Song-Playlist Relation'
        verbose_name_plural = 'Song-Playlist Relations'

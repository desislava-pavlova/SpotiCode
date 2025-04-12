import uuid
# Django
from django.db import models


class AlbumType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    album_type = models.CharField(db_column='album_type', verbose_name='Album Type')
    
    @classmethod
    def get_default_type(cls):
        type, created = cls.objects.get_or_create(album_type='Unknown')
        return type.id
    
    def __str__(self):
        return f'{self.album_type}'
    
    class Meta:
        db_table = 'album_types'
        ordering = ('album_type',)
        verbose_name = 'Album Type'
        verbose_name_plural = 'Album Types'


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True, 
                          db_column='id', verbose_name='ID')
    release_date = models.DateField(null=True, blank=True, 
                                    db_column='release_date', verbose_name='Release Date')
    album_name = models.CharField(db_column='album_name', verbose_name='Album')
    album_artist = models.ForeignKey(to='artists.Artist', to_field='id', on_delete=models.RESTRICT, 
                                     db_column='album_artist', verbose_name='Artist')
    album_type = models.ForeignKey(to='albums.AlbumType', default=AlbumType.get_default_type, 
                                   blank=True, on_delete=models.RESTRICT, 
                                  db_column='album_type', verbose_name='Album Type')
    
    def __str__(self):
        return f'"{self.album_name}" album by {self.album_artist.artist_name}'

    class Meta:
        db_table = 'albums'
        ordering = ('album_name', 'album_artist')
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'


class AlbumLink(models.Model):
    id = models.OneToOneField(to='albums.Album', to_field='id', on_delete=models.CASCADE, 
                              primary_key=True, 
                              db_column='id', verbose_name='ID')
    spotify_link = models.URLField(null=True, blank=True, 
                                   db_column='spotify_link', verbose_name='Spotify URL')
    wikipedia_link = models.URLField(null=True, blank=True, 
                                     db_column='wikipedia_link', verbose_name='Wikipedia URL')
    rateyourmusic_link = models.URLField(null=True, blank=True, unique=True, 
                                         db_column='rateyourmusic_link', verbose_name='Rate Your Music URL')
    
    def __str__(self):
        return f'Links for album: "{self.id.album_name}"'
    
    class Meta:
        db_table = 'albums_links'
        ordering = ('id',)
        verbose_name = 'Album Link'
        verbose_name_plural = 'Albums Links'

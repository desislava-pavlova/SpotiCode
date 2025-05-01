import uuid
# Django
from django.db import models


class Artist(models.Model):
    COUNTER_DEFAULT = 0
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    artist_name = models.CharField(unique=True, 
                                   db_column='artist_name', verbose_name='Artist')
    other_names = models.CharField(null=True, blank=True, 
                                   db_column='other_names', verbose_name='Other Names')
    date_formed = models.DateField(null=True, blank=True,
                                   db_column='date_formed', verbose_name='Date Formed')
    songs_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                      db_column='songs_count', verbose_name='Total Songs')
    albums_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                       db_column='albums_count', verbose_name='Total Albums')
    
    def __str__(self):
        return self.artist_name
    
    @classmethod
    def field_order(cls):
        return ['other_names', 'date_formed', 'songs_count', 'albums_count', 'id']
        

    class Meta:
        db_table = 'artists'
        ordering = ('artist_name',)
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class ArtistLink(models.Model):
    id = models.OneToOneField(Artist, to_field='id', on_delete=models.CASCADE, 
                              primary_key=True, 
                              db_column='id', verbose_name='ID')
    official_website = models.URLField(null=True, blank=True, unique=True, 
                                       db_column='official_website', verbose_name='Official Website')
    spotify_link = models.URLField(null=True, blank=True, unique=True, 
                                   db_column='spotify_link', verbose_name='Spotify Link')
    wikipedia_link = models.URLField(null=True, blank=True, unique=True, 
                                     db_column='wikipedia_link', verbose_name='Wikipedia Link')
    rateyourmusic_link = models.URLField(null=True, blank=True, unique=True, 
                                         db_column='rateyourmusic_link', verbose_name='Rate Your Music Link')

    def __str__(self):
        return f'Links for artist: {self.id.artist_name}'
    
    @classmethod
    def field_order(cls):
        return ['official_website', 'spotify_link', 'wikipedia_link', 'rateyourmusic_link']

    class Meta:
        db_table = 'artists_links'
        ordering = ('id',)
        verbose_name = 'Artist Link'
        verbose_name_plural = 'Artists Links'

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
    year_formed = models.PositiveIntegerField(null=True, blank=True,
                                              db_column='year_formed', verbose_name='Formed In')
    origin = models.CharField(null=True, blank=True, 
                              db_column='origin', verbose_name='Origin')
    songs_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                      db_column='songs_count', verbose_name='Total Songs')
    albums_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                       db_column='albums_count', verbose_name='Total Albums')
    
    def __str__(self):
        return self.artist_name
    
    @classmethod
    def field_order(cls):
        return ['other_names', 'year_formed', 'origin', 'songs_count', 'albums_count', 'id']
        

    class Meta:
        db_table = 'artists'
        ordering = ('artist_name',)
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class ArtistLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    for_artist = models.OneToOneField(Artist, to_field='id', on_delete=models.CASCADE, 
                              db_column='for_artist', verbose_name='For Artist')
    official_website = models.URLField(null=True, blank=True, unique=True, 
                                       db_column='official_website', verbose_name='Official Website')
    spotify_link = models.URLField(null=True, blank=True, unique=True, 
                                   db_column='spotify_link', verbose_name='Spotify Link')
    wikipedia_link = models.URLField(null=True, blank=True, unique=True, 
                                     db_column='wikipedia_link', verbose_name='Wikipedia Link')
    discogs_link = models.URLField(null=True, blank=True, unique=True,
                                   db_column='discogs_link', verbose_name='Discogs Link')
    rateyourmusic_link = models.URLField(null=True, blank=True, unique=True, 
                                         db_column='rateyourmusic_link', verbose_name='Rate Your Music Link')

    def __str__(self):
        return f'Links for artist: {self.for_artist.artist_name}'
    
    @classmethod
    def field_order(cls):
        return ['official_website', 'spotify_link', 'wikipedia_link', 'discogs_link', 'rateyourmusic_link']

    class Meta:
        db_table = 'artists_links'
        ordering = ('for_artist__artist_name',)
        verbose_name = 'Artist Link'
        verbose_name_plural = 'Artists Links'



# Missing data models
class MissingDataArtist(Artist):
    class Meta:
        proxy = True
        verbose_name = "Z_Missing Data: Artists"
        verbose_name_plural = "Z_Missing Data: Artists"


class MissingDataArtistLink(ArtistLink):
    class Meta:
        proxy = True
        verbose_name = "Z_Missing Data: Artists Links"
        verbose_name_plural = "Z_Missing Data: Artists Links"

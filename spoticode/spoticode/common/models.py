import uuid
# Django
from django.db import models


class MusicGroup(models.Model):
    GROUP_NAME_MAX_LENGTH = 100
    COUNTER_DEFAULT = 0
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    group_name = models.CharField(max_length=GROUP_NAME_MAX_LENGTH, unique=True, 
                                  db_column='group_name', verbose_name='Group Name')
    songs_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                      db_column='songs_count', verbose_name='Total Songs')
    pending_count = models.IntegerField(blank=True, default=COUNTER_DEFAULT, 
                                        db_column='pending_count', verbose_name='Pending Songs')
    
    def __str__(self):
        return self.group_name
    
    @classmethod
    def get_default_group(cls):
        group, created = cls.objects.get_or_create(group_name='Unspecified',
                                                    defaults={'id': uuid.uuid4()})
        return group.id

    class Meta:
        db_table = 'music_groups'
        ordering = ('group_name',)
        verbose_name = 'Music Group'
        verbose_name_plural = 'Music Groups'


class Genre(models.Model):
    GENRE_NAME_MAX_LENGTH = 100
    COUNTER_DEFAULT = 0
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True,
                          db_column='id', verbose_name='ID')
    genre_name = models.CharField(max_length=GENRE_NAME_MAX_LENGTH, unique=True, 
                                  db_column='genre_name', verbose_name='Genre')
    description = models.TextField(null=True, blank=True,
                                   db_column='description', verbose_name='Description')
    songs_count = models.IntegerField(default=COUNTER_DEFAULT, 
                                      db_column='songs_count', verbose_name='Total Songs')
    
    def __str__(self):
        return self.genre_name
    
    @classmethod
    def get_default_genre(cls):
        genre, created = cls.objects.get_or_create(genre_name='Unknown')
        return genre.id

    class Meta:
        db_table = 'genres'
        ordering = ('genre_name',)
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

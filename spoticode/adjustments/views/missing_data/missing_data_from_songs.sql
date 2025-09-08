CREATE OR REPLACE VIEW public.missing_data_from_songs
AS SELECT songs.id,
    artists.artist_name,
    songs.song_title,
    songs.song_year,
    genres.genre_name,
    albums.album_name
   FROM songs
     JOIN artists ON artists.id = songs.main_artist
     LEFT JOIN genres ON genres.id = songs.genre_id
     LEFT JOIN albums ON albums.id = songs.album_id
  WHERE songs.song_year IS NULL OR genres.genre_name IS NULL OR albums.album_name IS NULL
  ORDER BY artists.artist_name, songs.song_title;
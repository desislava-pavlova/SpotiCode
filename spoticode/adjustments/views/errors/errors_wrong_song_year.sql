-- public.errors_wrong_song_year source

CREATE OR REPLACE VIEW public.errors_wrong_song_year
AS SELECT songs.id AS song_id,
    songs.song_title,
    artists.artist_name AS main_artist,
    songs.feat_artist,
    songs.song_year,
    EXTRACT(year FROM albums.release_date) AS album_year,
    albums.album_name AS album
   FROM songs
     JOIN albums ON albums.id = songs.album_id
     JOIN artists ON artists.id = songs.main_artist
  WHERE EXTRACT(year FROM albums.release_date) < songs.song_year::numeric
  ORDER BY artists.artist_name, songs.song_title;
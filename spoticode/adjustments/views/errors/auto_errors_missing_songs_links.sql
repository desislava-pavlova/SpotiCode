-- public.auto_errors_missing_songs_links source

CREATE OR REPLACE VIEW public.auto_errors_missing_songs_links
AS SELECT songs.id AS song_id,
    songs.song_title,
    artists.artist_name AS artist,
    songs_links.id AS links_id
   FROM songs
     JOIN artists ON artists.id = songs.main_artist
     FULL JOIN songs_links ON songs_links.for_song = songs.id
  WHERE songs.id IS NULL OR songs_links.id IS NULL
  ORDER BY artists.artist_name, songs.song_title;
-- public.errors_wrong_song_links source

CREATE OR REPLACE VIEW public.errors_wrong_song_links
AS SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong file path'::text AS error_type,
    sl.file_path AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.file_path::text !~~ 'D:%'::text
UNION ALL
 SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong youtube video link'::text AS error_type,
    sl.youtube_video_link AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.youtube_video_link::text !~~ 'https://www.youtube.com/watch?v=%'::text
UNION ALL
 SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong youtube audio link'::text AS error_type,
    sl.youtube_audio_link AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.youtube_audio_link::text !~~ 'https://www.youtube.com/watch?v=%'::text
UNION ALL
 SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong spotify link'::text AS error_type,
    sl.spotify_link AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.spotify_link::text !~~ 'https://open.spotify.com/track/%'::text
UNION ALL
 SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong wikipedia link'::text AS error_type,
    sl.wikipedia_link AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.wikipedia_link::text !~~ 'https://en.wikipedia.org/?curid=%'::text
UNION ALL
 SELECT sl.id AS link_id,
    s.song_title,
    a.artist_name AS artist,
    'wrong rym link'::text AS error_type,
    sl.rateyourmusic_link AS wrong_link
   FROM songs_links sl
     JOIN songs s ON s.id = sl.for_song
     JOIN artists a ON a.id = s.main_artist
  WHERE sl.rateyourmusic_link::text !~~ 'https://rateyourmusic.com/song/%'::text
  ORDER BY 3, 2, 4;
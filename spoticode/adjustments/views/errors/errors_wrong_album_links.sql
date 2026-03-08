-- public.errors_wrong_album_links source

CREATE OR REPLACE VIEW public.errors_wrong_album_links
AS SELECT albl.id AS link_id,
    alb.album_name AS album,
    ar.artist_name AS artist,
    'wrong spotify link'::text AS error_type,
    albl.spotify_link AS wrong_link
   FROM albums_links albl
     JOIN albums alb ON alb.id = albl.for_album
     JOIN artists ar ON ar.id = alb.album_artist
  WHERE albl.spotify_link::text !~~ 'https://open.spotify.com/album/%'::text
UNION ALL
 SELECT albl.id AS link_id,
    alb.album_name AS album,
    ar.artist_name AS artist,
    'wrong wikipedia link'::text AS error_type,
    albl.wikipedia_link AS wrong_link
   FROM albums_links albl
     JOIN albums alb ON alb.id = albl.for_album
     JOIN artists ar ON ar.id = alb.album_artist
  WHERE albl.wikipedia_link::text !~~ 'https://en.wikipedia.org/?curid=%'::text
UNION ALL
 SELECT albl.id AS link_id,
    alb.album_name AS album,
    ar.artist_name AS artist,
    'wrong discogs link'::text AS error_type,
    albl.discogs_link AS wrong_link
   FROM albums_links albl
     JOIN albums alb ON alb.id = albl.for_album
     JOIN artists ar ON ar.id = alb.album_artist
  WHERE albl.discogs_link::text !~~ 'https://www.discogs.com/master/%'::text AND albl.discogs_link::text !~~ 'https://www.discogs.com/release/%'::text
UNION ALL
 SELECT albl.id AS link_id,
    alb.album_name AS album,
    ar.artist_name AS artist,
    'wrong rym link'::text AS error_type,
    albl.rateyourmusic_link AS wrong_link
   FROM albums_links albl
     JOIN albums alb ON alb.id = albl.for_album
     JOIN artists ar ON ar.id = alb.album_artist
  WHERE albl.rateyourmusic_link::text !~~ 'https://rateyourmusic.com/release/%'::text
  ORDER BY 3, 2, 4;
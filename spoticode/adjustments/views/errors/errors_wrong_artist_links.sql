-- public.errors_wrong_artist_links source

CREATE OR REPLACE VIEW public.errors_wrong_artist_links
AS SELECT al.id AS link_id,
    ar.artist_name AS artist,
    'wrong spotify link'::text AS error_type,
    al.spotify_link AS wrong_link
   FROM artists_links al
     JOIN artists ar ON ar.id = al.for_artist
  WHERE al.spotify_link::text !~~ 'https://open.spotify.com/artist/%'::text
UNION ALL
 SELECT al.id AS link_id,
    ar.artist_name AS artist,
    'wrong wikipedia link'::text AS error_type,
    al.wikipedia_link AS wrong_link
   FROM artists_links al
     JOIN artists ar ON ar.id = al.for_artist
  WHERE al.wikipedia_link::text !~~ 'https://en.wikipedia.org/?curid=%'::text
UNION ALL
 SELECT al.id AS link_id,
    ar.artist_name AS artist,
    'wrong discogs link'::text AS error_type,
    al.discogs_link AS wrong_link
   FROM artists_links al
     JOIN artists ar ON ar.id = al.for_artist
  WHERE al.discogs_link::text !~~ 'https://www.discogs.com/artist/%'::text
UNION ALL
 SELECT al.id AS link_id,
    ar.artist_name AS artist,
    'wrong rym link'::text AS error_type,
    al.rateyourmusic_link AS wrong_link
   FROM artists_links al
     JOIN artists ar ON ar.id = al.for_artist
  WHERE al.rateyourmusic_link::text !~~ 'https://rateyourmusic.com/artist/%'::text
  ORDER BY 2, 3;
CREATE OR REPLACE VIEW public.auto_errors_missing_artists_links
AS SELECT artists.id AS artist_id,
    artists.artist_name AS artist,
    artists_links.id AS links_id
   FROM artists
     FULL JOIN artists_links ON artists_links.for_artist = artists.id
  WHERE artists.id IS NULL OR artists_links.id IS NULL
  ORDER BY artists.artist_name;
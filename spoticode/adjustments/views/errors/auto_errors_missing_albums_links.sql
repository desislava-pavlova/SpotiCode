CREATE OR REPLACE VIEW public.auto_errors_missing_albums_links
AS SELECT albums.id AS album_id,
    artists.artist_name AS artist,
    albums.album_name AS album,
    links.id AS links_id
   FROM albums
     JOIN artists ON artists.id = albums.album_artist
     FULL JOIN albums_links links ON links.for_album = albums.id
  WHERE albums.id IS NULL OR links.id IS NULL
  ORDER BY artists.artist_name, albums.album_name;
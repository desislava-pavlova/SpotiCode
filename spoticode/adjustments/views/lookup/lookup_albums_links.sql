-- public.lookup_albums_links source

CREATE OR REPLACE VIEW public.lookup_albums_links
AS SELECT albums_links.id,
    artists.artist_name,
    albums.album_name,
    albums_links.spotify_link,
    albums_links.wikipedia_link,
    albums_links.rateyourmusic_link
   FROM albums_links
     JOIN albums ON albums_links.for_album = albums.id
     JOIN artists ON artists.id = albums.album_artist
  ORDER BY artists.artist_name, albums.album_name;
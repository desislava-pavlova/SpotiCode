-- public.lookup_albums source

CREATE OR REPLACE VIEW public.lookup_albums
AS SELECT albums.id,
    albums.release_date,
    albums.album_name,
    artists.artist_name AS album_artist,
    album_types.album_type,
    albums.songs_album,
    albums.songs_count
   FROM albums
     JOIN artists ON artists.id = albums.album_artist
     JOIN album_types ON album_types.id = albums.album_type
  ORDER BY artists.artist_name, albums.album_name;
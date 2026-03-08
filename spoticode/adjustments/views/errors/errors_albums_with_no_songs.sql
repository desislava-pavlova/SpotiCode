-- public.errors_albums_with_no_songs source

CREATE OR REPLACE VIEW public.errors_albums_with_no_songs
AS SELECT al.id,
    al.album_name,
    ar.artist_name
   FROM albums al
     JOIN artists ar ON ar.id = al.album_artist
     LEFT JOIN songs s ON al.id = s.album_id
  WHERE s.id IS NULL;
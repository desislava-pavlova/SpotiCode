-- public.errors_artists_with_no_songs source

CREATE OR REPLACE VIEW public.errors_artists_with_no_songs
AS SELECT ar.id,
    ar.artist_name
   FROM artists ar
     LEFT JOIN songs s ON ar.id = s.main_artist
  WHERE s.id IS NULL AND ar.artist_name::text <> 'Various Artists'::text;
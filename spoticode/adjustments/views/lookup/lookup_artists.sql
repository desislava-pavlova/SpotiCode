-- public.lookup_artists source

CREATE OR REPLACE VIEW public.lookup_artists
AS SELECT id,
    artist_name,
    other_names,
    songs_count,
    albums_count
   FROM artists
  ORDER BY artist_name;
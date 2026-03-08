-- public.lookup_genres source

CREATE OR REPLACE VIEW public.lookup_genres
AS SELECT id,
    genre_name,
    description,
    songs_count
   FROM genres
  ORDER BY genre_name;
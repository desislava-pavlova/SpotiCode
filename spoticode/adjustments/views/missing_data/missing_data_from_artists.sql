CREATE OR REPLACE VIEW public.missing_data_from_artists
AS SELECT id,
    artist_name,
    year_formed,
    origin
   FROM artists
  WHERE year_formed IS NULL OR origin IS NULL
  ORDER BY artist_name;
CREATE OR REPLACE VIEW public.view_total_songs_by_first_letter_artist
AS SELECT
        CASE
            WHEN upper("left"(art.artist_name::text, 1)) = ANY (ARRAY['0'::text, '1'::text, '2'::text, '3'::text, '4'::text, '5'::text, '6'::text, '7'::text, '8'::text, '9'::text]) THEN '0-9'::text
            ELSE upper("left"(art.artist_name::text, 1))
        END AS first_letter,
    count(*) AS counter
   FROM songs s
     JOIN artists art ON art.id = s.main_artist
  GROUP BY (
        CASE
            WHEN upper("left"(art.artist_name::text, 1)) = ANY (ARRAY['0'::text, '1'::text, '2'::text, '3'::text, '4'::text, '5'::text, '6'::text, '7'::text, '8'::text, '9'::text]) THEN '0-9'::text
            ELSE upper("left"(art.artist_name::text, 1))
        END)
  ORDER BY (
        CASE
            WHEN upper("left"(art.artist_name::text, 1)) = ANY (ARRAY['0'::text, '1'::text, '2'::text, '3'::text, '4'::text, '5'::text, '6'::text, '7'::text, '8'::text, '9'::text]) THEN '0-9'::text
            ELSE upper("left"(art.artist_name::text, 1))
        END);
-- public.auto_errors_wrong_calc_on_genres source

CREATE OR REPLACE VIEW public.auto_errors_wrong_calc_on_genres
AS WITH real_values AS (
         SELECT sub_g.genre_name,
            count(DISTINCT sub_s.id) AS real_songs
           FROM genres sub_g
             LEFT JOIN songs sub_s ON sub_s.genre_id = sub_g.id
          GROUP BY sub_g.genre_name
        )
 SELECT g.id,
    g.genre_name,
    g.songs_count,
    rv.real_songs
   FROM genres g
     JOIN real_values rv ON rv.genre_name::text = g.genre_name::text
  WHERE g.songs_count <> rv.real_songs
  ORDER BY g.genre_name;
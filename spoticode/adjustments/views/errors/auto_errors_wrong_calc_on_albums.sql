-- public.auto_errors_wrong_calc_on_albums source

CREATE OR REPLACE VIEW public.auto_errors_wrong_calc_on_albums
AS WITH real_values AS (
         SELECT sub_alb.id AS sub_id,
            count(DISTINCT sub_s.id) AS real_songs
           FROM albums sub_alb
             LEFT JOIN songs sub_s ON sub_s.album_id = sub_alb.id
          GROUP BY sub_alb.id
        )
 SELECT alb.id,
    alb.album_name AS album,
    art.artist_name AS artist,
    alb.songs_count AS auto_songs,
    rv.real_songs,
    alb.songs_album,
    alb.songs_count
   FROM albums alb
     JOIN real_values rv ON rv.sub_id = alb.id
     JOIN artists art ON art.id = alb.album_artist
  WHERE alb.songs_count <> rv.real_songs OR alb.songs_album IS NOT NULL AND alb.songs_album < alb.songs_count
  ORDER BY art.artist_name, alb.album_name;
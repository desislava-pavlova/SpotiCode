-- public.auto_errors_wrong_calc_on_artists source

CREATE OR REPLACE VIEW public.auto_errors_wrong_calc_on_artists
AS WITH real_values AS (
         SELECT sub_art.artist_name AS sub_artist,
            count(DISTINCT sub_s.id) AS real_songs,
            count(DISTINCT sub_alb.id) AS real_albums
           FROM artists sub_art
             LEFT JOIN songs sub_s ON sub_s.main_artist = sub_art.id
             LEFT JOIN albums sub_alb ON sub_alb.album_artist = sub_art.id
          GROUP BY sub_art.artist_name
        )
 SELECT art.id,
    art.artist_name AS artist,
    art.songs_count AS auto_songs,
    rv.real_songs,
    art.albums_count AS auto_albums,
    rv.real_albums
   FROM artists art
     JOIN real_values rv ON rv.sub_artist::text = art.artist_name::text
  WHERE art.songs_count <> rv.real_songs OR art.albums_count <> rv.real_albums
  ORDER BY art.artist_name;
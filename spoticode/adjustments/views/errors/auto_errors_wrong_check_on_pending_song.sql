CREATE OR REPLACE VIEW public.auto_errors_wrong_check_on_pending_song
AS WITH real_new_artists AS (
         SELECT sub1_ps.id AS sub1_id,
                CASE
                    WHEN sub1_art.artist_name IS NULL THEN true
                    ELSE false
                END AS real_new_artist
           FROM pending_songs sub1_ps
             LEFT JOIN artists sub1_art ON sub1_art.artist_name::text = sub1_ps.main_artist::text
        ), real_is_added_songs AS (
         SELECT sub2_ps.id AS sub2_id,
                CASE
                    WHEN sub2_s.song_title IS NOT NULL THEN true
                    ELSE false
                END AS real_is_added
           FROM pending_songs sub2_ps
             LEFT JOIN songs sub2_s ON lower(sub2_s.song_title::text) = lower(sub2_ps.song_title::text)
             JOIN artists sub2_art ON sub2_art.id = sub2_s.main_artist
          WHERE lower(sub2_art.artist_name::text) = lower(sub2_ps.main_artist::text)
        )
 SELECT ps.id,
    ps.song_title AS title,
    ps.main_artist AS artist,
    ps.feat_artist,
    ps.new_artist AS auto_new_artist,
    rna.real_new_artist,
    ps.is_added AS auto_is_added,
    rias.real_is_added
   FROM pending_songs ps
     JOIN real_new_artists rna ON rna.sub1_id = ps.id
     JOIN real_is_added_songs rias ON rias.sub2_id = ps.id
  WHERE ps.new_artist <> rna.real_new_artist OR ps.is_added <> rias.real_is_added
  ORDER BY ps.main_artist, ps.song_title;
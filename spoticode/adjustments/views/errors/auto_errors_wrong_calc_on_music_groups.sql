-- public.auto_errors_wrong_calc_on_music_groups source

CREATE OR REPLACE VIEW public.auto_errors_wrong_calc_on_music_groups
AS WITH real_values AS (
         SELECT mg_1.group_name,
            count(DISTINCT s.id) AS real_songs,
            count(DISTINCT ps.id) AS real_pending
           FROM music_groups mg_1
             LEFT JOIN songs s ON s.group_id = mg_1.id
             LEFT JOIN pending_songs ps ON ps.to_group = mg_1.id
          GROUP BY mg_1.group_name
        )
 SELECT mg.group_name,
    mg.songs_count,
    rv.real_songs,
    mg.pending_count,
    rv.real_pending
   FROM music_groups mg
     JOIN real_values rv ON rv.group_name::text = mg.group_name::text
  WHERE mg.songs_count <> rv.real_songs OR mg.pending_count <> rv.real_pending
  ORDER BY mg.group_name;
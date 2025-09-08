CREATE OR REPLACE VIEW public.lookup_music_groups
AS SELECT id,
    group_name,
    songs_count,
    pending_count
   FROM music_groups
  ORDER BY group_name;
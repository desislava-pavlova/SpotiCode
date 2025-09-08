CREATE OR REPLACE VIEW public.lookup_pending_songs
AS SELECT pending_songs.id,
    pending_songs.song_title,
    pending_songs.main_artist,
    pending_songs.feat_artist,
    music_groups.group_name AS to_group,
    pending_songs.is_added,
    pending_songs.new_artist
   FROM pending_songs
     JOIN music_groups ON music_groups.id = pending_songs.to_group
  ORDER BY pending_songs.main_artist, pending_songs.song_title;
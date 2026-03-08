-- public.view_total_links_by_music_group source

CREATE OR REPLACE VIEW public.view_total_links_by_music_group
AS SELECT mg.group_name AS "Group",
    count(s.id) AS "Songs",
    count(sl.file_path) AS "File Paths",
    count(sl.spotify_link) AS "Spotify",
    count(sl.youtube_video_link) AS "YouTube Videos",
    count(sl.youtube_audio_link) AS "YouTube Audios",
    count(sl.wikipedia_link) AS "Wikipedia",
    count(sl.rateyourmusic_link) AS "Rate Your Music"
   FROM music_groups mg
     JOIN songs s ON s.group_id = mg.id
     JOIN songs_links sl ON sl.for_song = s.id
  GROUP BY mg.group_name
  ORDER BY mg.group_name;
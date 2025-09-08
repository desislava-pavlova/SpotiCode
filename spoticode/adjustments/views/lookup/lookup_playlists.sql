CREATE OR REPLACE VIEW public.lookup_playlists
AS SELECT id,
    playlist_name,
    songs_count,
    spotify_count,
    playlist_link,
    playlist_image,
    notes
   FROM playlists p
  ORDER BY playlist_name;
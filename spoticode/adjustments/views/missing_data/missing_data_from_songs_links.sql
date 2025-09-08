CREATE OR REPLACE VIEW public.missing_data_from_songs_links
AS SELECT songs_links.id,
    artists.artist_name,
    songs_links.youtube_video_link,
    songs_links.youtube_audio_link,
    songs_links.spotify_link,
    songs_links.wikipedia_link,
    songs_links.rateyourmusic_link
   FROM songs_links
     JOIN songs ON songs.id = songs_links.for_song
     JOIN artists ON artists.id = songs.main_artist
  WHERE songs_links.youtube_video_link IS NULL OR songs_links.youtube_audio_link IS NULL OR songs_links.spotify_link IS NULL OR songs_links.wikipedia_link IS NULL OR songs_links.rateyourmusic_link IS NULL
  ORDER BY artists.artist_name, songs.song_title;
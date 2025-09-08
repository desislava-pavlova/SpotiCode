CREATE OR REPLACE VIEW public.lookup_songs_links
AS SELECT songs_links.id,
    songs.song_title,
    artists.artist_name,
    songs_links.spotify_link,
    songs_links.wikipedia_link,
    songs_links.rateyourmusic_link
   FROM songs_links
     JOIN songs ON songs.id = songs_links.for_song
     JOIN artists ON artists.id = songs.main_artist
  ORDER BY artists.artist_name, songs.song_title;
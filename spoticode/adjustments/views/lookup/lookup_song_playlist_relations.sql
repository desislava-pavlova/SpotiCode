-- public.lookup_song_playlist_relations source

CREATE OR REPLACE VIEW public.lookup_song_playlist_relations
AS SELECT song_playlist_relations.id,
    playlists.playlist_name,
    songs.song_title,
    artists.artist_name
   FROM song_playlist_relations
     JOIN playlists ON playlists.id = song_playlist_relations.playlist_id
     JOIN songs ON songs.id = song_playlist_relations.song_id
     JOIN artists ON artists.id = songs.main_artist
  ORDER BY playlists.playlist_name, artists.artist_name, songs.song_title;
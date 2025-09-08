ALTER TABLE song_playlist_relations DROP CONSTRAINT song_playlist_relations_playlist_id_f5dcd914_fk_playlists_id;
ALTER TABLE song_playlist_relations ADD CONSTRAINT song_playlist_relations_playlist_id_f5dcd914_fk_playlists_id 
	FOREIGN KEY (playlist_id) REFERENCES public.playlists(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE song_playlist_relations DROP CONSTRAINT song_playlist_relations_song_id_f8b3eefa_fk_songs_id;
ALTER TABLE song_playlist_relations ADD CONSTRAINT song_playlist_relations_song_id_f8b3eefa_fk_songs_id 
	FOREIGN KEY (song_id) REFERENCES public.songs(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
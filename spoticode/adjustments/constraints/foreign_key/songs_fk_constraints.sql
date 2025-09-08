ALTER TABLE songs DROP CONSTRAINT songs_album_id_c9f108d1_fk_albums_id;
ALTER TABLE songs ADD CONSTRAINT songs_album_id_c9f108d1_fk_albums_id 
	FOREIGN KEY (album_id) REFERENCES public.albums(id) ON DELETE SET NULL ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE songs DROP CONSTRAINT songs_genre_30e45caf_fk_genres_id;
ALTER TABLE songs ADD CONSTRAINT songs_genre_30e45caf_fk_genres_id 
	FOREIGN KEY (genre_id) REFERENCES public.genres(id) ON DELETE SET NULL ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE songs DROP CONSTRAINT songs_group_id_56831242_fk_music_groups_id;
ALTER TABLE songs ADD CONSTRAINT songs_group_id_56831242_fk_music_groups_id 
	FOREIGN KEY (group_id) REFERENCES public.music_groups(id) ON DELETE SET DEFAULT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE songs DROP CONSTRAINT songs_main_artist_8f2b9ace_fk_artists_id;
ALTER TABLE songs ADD CONSTRAINT songs_main_artist_8f2b9ace_fk_artists_id 
	FOREIGN KEY (main_artist) REFERENCES public.artists(id) ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
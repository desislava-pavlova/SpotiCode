ALTER TABLE songs_links DROP CONSTRAINT songs_links_for_song_a04c98bf_fk_songs_id;
ALTER TABLE songs_links ADD CONSTRAINT songs_links_for_song_a04c98bf_fk_songs_id 
	FOREIGN KEY (for_song) REFERENCES public.songs(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
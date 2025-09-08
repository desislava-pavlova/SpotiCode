ALTER TABLE pending_songs DROP CONSTRAINT pending_songs_to_group_e06b2f06_fk_music_groups_id;
ALTER TABLE pending_songs ADD CONSTRAINT pending_songs_to_group_e06b2f06_fk_music_groups_id 
	FOREIGN KEY (to_group) REFERENCES public.music_groups(id) ON DELETE SET DEFAULT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

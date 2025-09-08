ALTER TABLE albums_links DROP CONSTRAINT albums_links_for_album_9c08a286_fk_albums_id;
ALTER TABLE albums_links ADD CONSTRAINT albums_links_for_album_9c08a286_fk_albums_id 
	FOREIGN KEY (for_album) REFERENCES public.albums(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
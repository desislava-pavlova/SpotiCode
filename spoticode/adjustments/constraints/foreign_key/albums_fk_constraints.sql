ALTER TABLE albums DROP CONSTRAINT albums_album_artist_85c52754_fk_artists_id;
ALTER TABLE albums ADD CONSTRAINT albums_album_artist_85c52754_fk_artists_id 
	FOREIGN KEY (album_artist) REFERENCES public.artists(id) ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE albums DROP CONSTRAINT albums_album_type_fa6a1333_fk_album_types_id;
ALTER TABLE albums ADD CONSTRAINT albums_album_type_fa6a1333_fk_album_types_id 
	FOREIGN KEY (album_type) REFERENCES public.album_types(id) ON DELETE SET DEFAULT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
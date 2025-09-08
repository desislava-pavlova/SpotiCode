ALTER TABLE artists_links DROP CONSTRAINT artists_links_for_artist_fk_artists_id;
ALTER TABLE artists_links ADD CONSTRAINT artists_links_for_artist_fk_artists_id 
	FOREIGN KEY (for_artist) REFERENCES public.artists(id) ON DELETE CASCADE ON UPDATE CASCADE;
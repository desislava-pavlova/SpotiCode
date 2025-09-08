CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_sp_relations()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- 1.1) calc OLD songs
				UPDATE
					playlists 
				SET
					songs_count = (
						SELECT 
							COUNT(*)
						FROM
							song_playlist_relations
						WHERE 
							playlist_id = OLD.playlist_id
						)
				WHERE 
					id = OLD.playlist_id;
			
			-- 1.2) calc OLD spotify_links
				UPDATE
					playlists 
				SET
					spotify_count = (
						SELECT 
							COUNT(sl.spotify_link)
						FROM
							song_playlist_relations spr
						JOIN songs s
							ON s.id = spr.song_id
						JOIN songs_links sl
							ON sl.for_song = s.id
						WHERE 
							spr.playlist_id = OLD.playlist_id
							AND sl.spotify_link IS NOT NULL
						)
				WHERE 
					id = OLD.playlist_id;
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- 2.1) calc NEW songs
			UPDATE
				playlists 
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						song_playlist_relations
					WHERE 
						playlist_id = NEW.playlist_id
					)
			WHERE 
				id = NEW.playlist_id;
			
			-- 2.2) calc NEW spotify_links
			UPDATE
				playlists 
			SET
				spotify_count = (
					SELECT 
						COUNT(sl.spotify_link)
					FROM
						song_playlist_relations spr
					JOIN songs s
						ON s.id = spr.song_id
					JOIN songs_links sl
						ON sl.for_song = s.id
					WHERE 
						spr.playlist_id = NEW.playlist_id
						AND sl.spotify_link IS NOT NULL
					)
			WHERE 
				id = NEW.playlist_id;
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
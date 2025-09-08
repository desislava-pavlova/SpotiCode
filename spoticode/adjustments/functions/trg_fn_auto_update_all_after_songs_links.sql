CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_songs_links()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- 1.1) calc OLD links
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
						spr.playlist_id = playlists.id
				    	AND sl.spotify_link IS NOT NULL
					)
			WHERE EXISTS (
				SELECT 
					1
				FROM 
					song_playlist_relations spr 
				WHERE 
					spr.song_id = OLD.for_song
				);
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- 2.1) calc NEW songs
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
						spr.playlist_id = playlists.id
				    	AND sl.spotify_link IS NOT NULL
					)
			WHERE EXISTS (
				SELECT 
					1
				FROM 
					song_playlist_relations spr 
				WHERE 
					spr.song_id = NEW.for_song
				);
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
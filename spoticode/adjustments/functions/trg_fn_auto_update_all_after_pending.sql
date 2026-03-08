-- DROP FUNCTION public.trg_fn_auto_update_all_after_pending();

CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_pending()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- Old-1) calc OLD groups
			UPDATE
				music_groups 
			SET
				pending_count = (
					SELECT 
						COUNT(*)
					FROM
						pending_songs
					WHERE 
						to_group = OLD.to_group
					)
			WHERE 
				id = OLD.to_group;
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- New-1) calc NEW groups
			UPDATE
				music_groups 
			SET
				pending_count = (
					SELECT 
						COUNT(*)
					FROM
						pending_songs
					WHERE 
						to_group = NEW.to_group
					)
			WHERE 
				id = NEW.to_group;

			-- New-2) check NEW pending_artists
			IF EXISTS (
				SELECT 
					1
				FROM 
					artists 
				WHERE 
			        artist_name = NEW.main_artist
				) 
			THEN
				UPDATE
					pending_songs 
				SET
					new_artist = FALSE
				WHERE
					main_artist = NEW.main_artist;
			ELSE
			    UPDATE 
			    	pending_songs 
			    SET 
			    	new_artist = TRUE 
			    WHERE 
			        main_artist = NEW.main_artist;
			END IF;
			
			-- New-2) check NEW pending_songs
			IF EXISTS (
				SELECT 
					1
				FROM 
					songs 
				JOIN artists 
					ON artists.id = songs.main_artist
				WHERE 
		        	song_title = NEW.song_title
		        	AND artists.artist_name = NEW.main_artist
				) 
			THEN
				UPDATE
					pending_songs 
				SET
					is_added = TRUE
				WHERE
					main_artist = NEW.main_artist;
			ELSE
			    UPDATE 
			    	pending_songs 
			    SET 
			    	is_added = FALSE 
			    WHERE 
			        main_artist = NEW.main_artist;
			END IF;
		
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
;

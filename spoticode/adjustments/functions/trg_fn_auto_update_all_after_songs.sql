CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_songs()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- Old-1) calc OLD artists
			UPDATE
				artists
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						main_artist = OLD.main_artist
					)
			WHERE 
				id = OLD.main_artist;
		
			-- Old-2) calc OLD groups
			UPDATE
				music_groups  
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						group_id = OLD.group_id
					)
			WHERE 
				id = OLD.group_id;
			
			-- Old-3) calc OLD genres
			UPDATE
				genres 
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						genre_id = OLD.genre_id
					)
			WHERE 
				id = OLD.genre_id;
	
	
			-- Old-4) calc OLD albums
			UPDATE
				albums 
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						album_id = OLD.album_id
					)
			WHERE 
				id = OLD.album_id;
	
			
			-- Old-5) check OLD pending
			IF EXISTS (
				SELECT 
					1
				FROM 
					songs 
				WHERE 
		        	songs.song_title = OLD.song_title
		        	AND main_artist = OLD.main_artist
			) THEN
				UPDATE
					pending_songs 
				SET
					is_added = TRUE
				WHERE
					song_title = OLD.song_title
		        	AND main_artist = (
						SELECT artist_name FROM artists WHERE id = OLD.main_artist
						);
		    ELSE
		    	UPDATE 
		    		pending_songs 
		    	SET 
		    		is_added = FALSE 
		    	WHERE
					song_title = OLD.song_title
		        	AND main_artist = (
						SELECT artist_name FROM artists WHERE id = OLD.main_artist
						);
			END IF;
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- New-1) calc NEW artists
			UPDATE
				artists
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						main_artist = NEW.main_artist
					)
			WHERE 
				id = NEW.main_artist;
	
			-- New-2) calc NEW groups
			UPDATE
				music_groups  
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						group_id = NEW.group_id
					)
			WHERE 
				id = NEW.group_id;
		
			-- New-3) calc NEW genres
			UPDATE
				genres 
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						genre_id = NEW.genre_id
					)
			WHERE 
				id = NEW.genre_id;
	
	
			-- New-4) calc NEW albums
			UPDATE
				albums 
			SET
				songs_count = (
					SELECT 
						COUNT(*)
					FROM
						songs
					WHERE 
						album_id = NEW.album_id
					)
			WHERE 
				id = NEW.album_id;			
	
			-- New-5) check NEW pending
			IF EXISTS (
				SELECT 
					1
				FROM 
					songs 
				WHERE 
		        	songs.song_title = NEW.song_title
		        	AND main_artist = NEW.main_artist
				) 
			THEN
				UPDATE
					pending_songs 
				SET
					is_added = TRUE
				WHERE
					song_title = NEW.song_title
		        	AND main_artist = (
						SELECT artist_name FROM artists WHERE id = NEW.main_artist
						);
		    ELSE
		    	UPDATE 
		    		pending_songs 
		    	SET 
		    		is_added = FALSE 
		    	WHERE
					song_title = NEW.song_title
		        	AND main_artist = (
						SELECT artist_name FROM artists WHERE id = NEW.main_artist
						);
			END IF;

			-- New-6) insert NEW links
			IF NOT EXISTS (
				SELECT 
					1
				FROM 
					songs_links 
				WHERE 
					songs_links.for_song = NEW.id
			) THEN 
				INSERT INTO songs_links (id, for_song)
						VALUES
							(gen_random_uuid(), NEW.id);
			END IF;
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
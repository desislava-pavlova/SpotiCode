-- DROP FUNCTION public.trg_fn_auto_update_all_after_artists();

CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_artists()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- 1.1) check OLD pending
			IF EXISTS (
				SELECT 
					1
				FROM 
					artists 
				WHERE 
			        artist_name = OLD.artist_name
				) 
			THEN
				UPDATE
					pending_songs 
				SET
					new_artist = FALSE
				WHERE
					main_artist = OLD.artist_name;
			ELSE
			    UPDATE 
			    	pending_songs 
			    SET 
			    	new_artist = TRUE 
			    WHERE 
			        main_artist = OLD.artist_name;
			END IF;
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- 2.1) check NEW pending
			IF EXISTS (
				SELECT 
					1
				FROM 
					artists 
				WHERE 
			        artist_name = NEW.artist_name
				) 
			THEN
				UPDATE
					pending_songs 
				SET
					new_artist = FALSE
				WHERE
					main_artist = NEW.artist_name;
			ELSE
			    UPDATE 
			    	pending_songs 
			    SET 
			    	new_artist = TRUE 
			    WHERE 
			        main_artist = NEW.artist_name;
			END IF;
			
			-- 2.2) insert NEW links
			IF NOT EXISTS (
				SELECT 
					1
				FROM 
					artists_links 
				WHERE 
		        	artists_links.for_artist = NEW.id
			) THEN
				INSERT INTO artists_links (id, for_artist)
					VALUES
						(uuid_generate_v4(), NEW.id);
			END IF;
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
;

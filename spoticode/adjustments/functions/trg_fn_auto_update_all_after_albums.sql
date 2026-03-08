-- DROP FUNCTION public.trg_fn_auto_update_all_after_albums();

CREATE OR REPLACE FUNCTION public.trg_fn_auto_update_all_after_albums()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		
		-- 1) All OLD values after UPDATE or DELETE;
		IF TG_OP = 'DELETE' OR TG_OP = 'UPDATE' THEN
		
			-- 1.1) calc OLD artists
			UPDATE
				artists
			SET
				albums_count = (
					SELECT 
						COUNT(*)
					FROM
						albums
					WHERE 
						album_artist = OLD.album_artist
					)
			WHERE 
				id = OLD.album_artist;
		END IF;


		-- 2) All NEW values after INSERT or UPDATE;
		IF TG_OP = 'INSERT' OR TG_OP = 'UPDATE' THEN
		
			-- 2.1) calc NEW artists
			UPDATE
				artists
			SET
				albums_count = (
					SELECT 
						COUNT(*)
					FROM
						albums
					WHERE 
						album_artist = NEW.album_artist
					)
			WHERE 
				id = NEW.album_artist;
			
			-- 2.2) insert NEW links
			IF NOT EXISTS (
				SELECT 
					1
				FROM 
					albums_links 
				WHERE 
		        	albums_links.for_album = NEW.id
			) THEN
				INSERT INTO albums_links (id, for_album)
					VALUES
						(uuid_generate_v4(), NEW.id);
			END IF;
		END IF;

	RETURN COALESCE(NEW, OLD);
END;
$function$
;

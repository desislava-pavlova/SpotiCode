CREATE OR REPLACE FUNCTION public.def_fn_get_unknown_album_type()
 RETURNS uuid
 LANGUAGE plpgsql
AS $function$
DECLARE
    result UUID;
BEGIN
    SELECT id INTO result
    FROM album_types
    WHERE album_type = 'Unknown'
    LIMIT 1;

    -- If not found, insert it
    IF result IS NULL THEN
        INSERT INTO album_types (album_type)
        VALUES ('Unknown')
        RETURNING id INTO result;
    END IF;

    RETURN result;
END;
$function$
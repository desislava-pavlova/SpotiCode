CREATE OR REPLACE FUNCTION public.def_fn_get_unspecified_group()
 RETURNS uuid
 LANGUAGE plpgsql
AS $function$
DECLARE
    result UUID;
BEGIN
    SELECT id INTO result
    FROM music_groups
    WHERE group_name = 'Unspecified'
    LIMIT 1;

    -- If not found, insert it
    IF result IS NULL THEN
        INSERT INTO music_groups (group_name)
        VALUES ('Unspecified')
        RETURNING id INTO result;
    END IF;

    RETURN result;
END;
$function$
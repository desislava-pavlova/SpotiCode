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

    RETURN result;
END;
$function$
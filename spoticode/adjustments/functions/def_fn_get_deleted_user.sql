CREATE OR REPLACE FUNCTION public.def_fn_get_deleted_user()
 RETURNS integer
 LANGUAGE plpgsql
AS $function$
DECLARE
    result int;
BEGIN
    SELECT id INTO result
    FROM auth_user
    WHERE username = 'deleted.user'
    LIMIT 1;

    RETURN result;
END;
$function$
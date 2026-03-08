CREATE OR REPLACE FUNCTION public.all_errors_summary()
 RETURNS TABLE(view_name text, error_count bigint)
 LANGUAGE plpgsql
AS $function$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT table_schema, table_name
        FROM information_schema.views
        WHERE table_name LIKE 'auto_errors_%'
           OR table_name LIKE 'errors_%'
    LOOP
        RETURN QUERY EXECUTE format(
            'SELECT %L, COUNT(*) FROM %I.%I',
            r.table_name,
            r.table_schema,
            r.table_name
        );
    END LOOP;
END;
$function$
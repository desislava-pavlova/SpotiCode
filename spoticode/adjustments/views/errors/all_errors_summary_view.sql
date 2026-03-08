-- public.all_errors_summary_view source

CREATE OR REPLACE VIEW public.all_errors_summary_view
AS SELECT view_name,
    error_count
   FROM all_errors_summary() all_errors_summary(view_name, error_count)
  WHERE error_count > 0
  ORDER BY view_name;
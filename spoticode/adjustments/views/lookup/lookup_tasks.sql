-- public.lookup_tasks source

CREATE OR REPLACE VIEW public.lookup_tasks
AS SELECT id,
    to_char(date_created, 'YYYY-MM-DD | HH24:MI'::text) AS date_created,
    to_char(last_modified, 'YYYY-MM-DD | HH24:MI'::text) AS last_modified,
    to_char(date_closed, 'YYYY-MM-DD | HH24:MI'::text) AS date_closed,
    task_name,
    related_app,
    responsible,
    status,
    priority,
    task_type,
    description
   FROM tasks
  ORDER BY (
        CASE
            WHEN status::text = 'Not Started'::text THEN 1
            WHEN status::text = 'In Progress'::text THEN 2
            WHEN status::text = 'Needs Assistance'::text THEN 3
            WHEN status::text = 'Issues Found'::text THEN 4
            WHEN status::text = 'On Hold'::text THEN 5
            WHEN status::text = 'For Testing'::text THEN 6
            WHEN status::text = 'Completed'::text THEN 7
            WHEN status::text = 'Cancelled'::text THEN 8
            ELSE NULL::integer
        END), related_app, priority, (to_char(date_created, 'YYYY-MM-DD | HH24:MI'::text));
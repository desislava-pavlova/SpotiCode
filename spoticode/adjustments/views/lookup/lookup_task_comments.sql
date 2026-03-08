-- public.lookup_task_comments source

CREATE OR REPLACE VIEW public.lookup_task_comments
AS SELECT task_comments.id,
    task_comments.comment_text,
    task_comments."user",
    to_char(task_comments.date_created, 'YYYY-MM-DD | HH24:MI'::text) AS date_created,
    tasks.task_name AS for_task,
    tasks.status
   FROM task_comments
     JOIN tasks ON tasks.id = task_comments.task_id
  ORDER BY (
        CASE
            WHEN tasks.status::text = 'Not Started'::text THEN 1
            WHEN tasks.status::text = 'In Progress'::text THEN 2
            WHEN tasks.status::text = 'Needs Assistance'::text THEN 3
            WHEN tasks.status::text = 'Issues Found'::text THEN 4
            WHEN tasks.status::text = 'On Hold'::text THEN 5
            WHEN tasks.status::text = 'For Testing'::text THEN 6
            WHEN tasks.status::text = 'Completed'::text THEN 7
            WHEN tasks.status::text = 'Cancelled'::text THEN 8
            ELSE NULL::integer
        END), tasks.id, task_comments.date_created;
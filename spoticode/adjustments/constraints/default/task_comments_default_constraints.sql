CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE task_comments ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE task_comments ALTER COLUMN user SET DEFAULT def_fn_get_deleted_user();
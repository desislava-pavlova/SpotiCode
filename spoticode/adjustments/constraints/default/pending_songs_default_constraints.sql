CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE pending_songs ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE pending_songs ALTER COLUMN is_added SET DEFAULT 'false';
ALTER TABLE pending_songs ALTER COLUMN new_artist SET DEFAULT 'false';
ALTER TABLE pending_songs ALTER COLUMN to_group SET DEFAULT def_fn_get_unspecified_group();
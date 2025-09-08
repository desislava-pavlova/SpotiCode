CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE songs ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE songs ALTER COLUMN group_id SET DEFAULT def_fn_get_unspecified_group();
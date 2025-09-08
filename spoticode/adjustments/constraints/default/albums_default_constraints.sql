CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE albums ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE albums ALTER COLUMN album_type SET DEFAULT def_fn_get_unknown_album_type();
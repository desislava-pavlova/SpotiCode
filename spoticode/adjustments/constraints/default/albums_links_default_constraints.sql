CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE albums_links ALTER COLUMN id SET DEFAULT uuid_generate_v4();
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE artists_links ALTER COLUMN id SET DEFAULT uuid_generate_v4();
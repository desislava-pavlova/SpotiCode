CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE album_types ALTER COLUMN id SET DEFAULT uuid_generate_v4();
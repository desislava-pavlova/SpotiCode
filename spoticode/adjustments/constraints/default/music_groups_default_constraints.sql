CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE music_groups ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE music_groups ALTER COLUMN songs_count SET DEFAULT '0';
ALTER TABLE music_groups ALTER COLUMN pending_count SET DEFAULT '0';
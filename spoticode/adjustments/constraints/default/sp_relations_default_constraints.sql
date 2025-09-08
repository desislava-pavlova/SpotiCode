CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE song_playlist_relations ALTER COLUMN id SET DEFAULT uuid_generate_v4();
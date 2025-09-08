CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE playlists ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE playlists ALTER COLUMN songs_count SET DEFAULT '0';
ALTER TABLE playlists ALTER COLUMN spotify_count SET DEFAULT '0';
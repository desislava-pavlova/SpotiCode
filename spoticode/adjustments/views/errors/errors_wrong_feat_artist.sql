-- public.errors_wrong_feat_artist source

CREATE OR REPLACE VIEW public.errors_wrong_feat_artist
AS SELECT songs.id AS song_id,
    songs.song_title,
    main_art.artist_name AS main_artist,
    songs.feat_artist,
    artists.artist_name AS name_from_artist,
    unnested.feat_artist_part AS feat_name
   FROM songs
     JOIN artists main_art ON main_art.id = songs.main_artist
     JOIN LATERAL ( SELECT regexp_split_to_table(songs.feat_artist::text, '\s*(,|&)\s*'::text) AS feat_artist_part) unnested ON true
     JOIN artists ON lower(TRIM(BOTH FROM unnested.feat_artist_part)) = lower(artists.artist_name::text)
  WHERE songs.feat_artist IS NOT NULL AND songs.feat_artist::text !~~ (('%'::text || artists.artist_name::text) || '%'::text);
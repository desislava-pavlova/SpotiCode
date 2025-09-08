CREATE OR REPLACE VIEW public.lookup_songs
AS SELECT s.id AS "ID",
    s.song_title AS "Title",
    ar.artist_name AS "Artist",
    s.feat_artist AS "Feat Artist",
    s.song_year AS "Year",
    g.genre_name AS "Genre",
    al.album_name AS "Album",
    mg.group_name AS "Group"
   FROM songs s
     JOIN artists ar ON ar.id = s.main_artist
     LEFT JOIN genres g ON g.id = s.genre_id
     LEFT JOIN albums al ON al.id = s.album_id
     LEFT JOIN music_groups mg ON mg.id = s.group_id
  ORDER BY ar.artist_name, s.song_title;
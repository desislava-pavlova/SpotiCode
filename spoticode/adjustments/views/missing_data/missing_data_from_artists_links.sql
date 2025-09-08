CREATE OR REPLACE VIEW public.missing_data_from_artists_links
AS SELECT artists_links.id,
    artists.artist_name,
    artists_links.official_website,
    artists_links.spotify_link,
    artists_links.wikipedia_link,
    artists_links.rateyourmusic_link
   FROM artists_links
     JOIN artists ON artists.id = artists_links.for_artist
  WHERE artists_links.official_website IS NULL OR artists_links.spotify_link IS NULL OR artists_links.wikipedia_link IS NULL OR artists_links.rateyourmusic_link IS NULL
  ORDER BY artists.artist_name;
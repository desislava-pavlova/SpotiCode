CREATE TRIGGER trg_songs_links_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    ON
    public.songs_links FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_songs_links()
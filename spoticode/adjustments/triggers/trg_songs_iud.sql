CREATE TRIGGER trg_songs_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    ON
    public.songs FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_songs();
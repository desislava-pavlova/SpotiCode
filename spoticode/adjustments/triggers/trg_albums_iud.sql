CREATE TRIGGER trg_albums_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    ON
    public.albums FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_albums()
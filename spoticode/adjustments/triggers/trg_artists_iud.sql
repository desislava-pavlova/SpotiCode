CREATE TRIGGER trg_artists_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    ON
    public.artists FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_artists()
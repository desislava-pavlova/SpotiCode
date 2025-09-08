CREATE TRIGGER trg_pending_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    OF song_title,
    main_artist,
    to_group ON
    public.pending_songs FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_pending();
CREATE TRIGGER trg_song_playlist_relations_iud AFTER
INSERT
    OR
DELETE
    OR
UPDATE
    ON
    public.song_playlist_relations FOR EACH ROW EXECUTE FUNCTION trg_fn_auto_update_all_after_sp_relations()
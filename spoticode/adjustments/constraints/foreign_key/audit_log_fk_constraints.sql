ALTER TABLE audit_log DROP CONSTRAINT audit_log_user_fc670273_fk_auth_user_id;
ALTER TABLE audit_log ADD CONSTRAINT audit_log_user_fc670273_fk_auth_user_id 
	FOREIGN KEY ("user") REFERENCES public.auth_user(id) ON DELETE SET DEFAULT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
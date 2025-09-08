ALTER TABLE tasks DROP CONSTRAINT tasks_responsible_3ab198ce_fk_auth_user_username;
ALTER TABLE tasks ADD CONSTRAINT tasks_responsible_3ab198ce_fk_auth_user_username 
	FOREIGN KEY (responsible) REFERENCES public.auth_user(username) ON DELETE SET NULL ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
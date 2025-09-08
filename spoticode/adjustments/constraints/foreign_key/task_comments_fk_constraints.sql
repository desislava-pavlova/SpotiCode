ALTER TABLE task_comments DROP CONSTRAINT task_comments_task_id_774b925c_fk_tasks_id;
ALTER TABLE task_comments ADD CONSTRAINT task_comments_task_id_774b925c_fk_tasks_id 
	FOREIGN KEY (task_id) REFERENCES public.tasks(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE task_comments DROP CONSTRAINT task_comments_user_f897d0f0_fk_auth_user_username;
ALTER TABLE task_comments ADD CONSTRAINT task_comments_user_f897d0f0_fk_auth_user_username 
	FOREIGN KEY ("user") REFERENCES public.auth_user(username) ON DELETE SET DEFAULT ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED;
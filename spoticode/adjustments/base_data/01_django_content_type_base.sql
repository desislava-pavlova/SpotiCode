DELETE FROM public.auth_permission;

DELETE FROM public.django_content_type;

INSERT INTO public.django_content_type (id,app_label,model) VALUES
	 (1,'admin','logentry'),
	 (2,'auth','permission'),
	 (3,'auth','group'),
	 (4,'auth','user'),
	 (5,'contenttypes','contenttype'),
	 (6,'sessions','session'),
	 (7,'albums','album'),
	 (8,'albums','albumtype'),
	 (9,'albums','albumlink'),
	 (10,'artists','artist'),
	 (11,'artists','artistlink'),
	 (12,'common','genre'),
	 (13,'common','musicgroup'),
	 (14,'playlists','playlist'),
	 (15,'playlists','songplaylistrelation'),
	 (16,'songs','pendingsong'),
	 (17,'songs','song'),
	 (18,'tasks','task'),
	 (19,'tasks','taskcomment'),
	 (20,'auditlog','auditlog'),
	 (21,'songs','songlink'),
	 (22,'artists','missingdataartist'),
	 (23,'albums','missingdataalbum'),
	 (24,'albums','missingdataalbumlink'),
	 (25,'artists','missingdataartistlink'),
	 (26,'songs','missingdatasong'),
	 (27,'songs','missingdatasonglink');

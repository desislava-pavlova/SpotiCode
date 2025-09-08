DELETE FROM public.auth_permission;

INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (1,'Can add log entry',1,'add_logentry'),
	 (2,'Can change log entry',1,'change_logentry'),
	 (3,'Can delete log entry',1,'delete_logentry'),
	 (4,'Can view log entry',1,'view_logentry'),
	 (5,'Can add permission',2,'add_permission'),
	 (6,'Can change permission',2,'change_permission'),
	 (7,'Can delete permission',2,'delete_permission'),
	 (8,'Can view permission',2,'view_permission'),
	 (9,'Can add group',3,'add_group'),
	 (10,'Can change group',3,'change_group');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (11,'Can delete group',3,'delete_group'),
	 (12,'Can view group',3,'view_group'),
	 (13,'Can add user',4,'add_user'),
	 (14,'Can change user',4,'change_user'),
	 (15,'Can delete user',4,'delete_user'),
	 (16,'Can view user',4,'view_user'),
	 (17,'Can add content type',5,'add_contenttype'),
	 (18,'Can change content type',5,'change_contenttype'),
	 (19,'Can delete content type',5,'delete_contenttype'),
	 (20,'Can view content type',5,'view_contenttype');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (21,'Can add session',6,'add_session'),
	 (22,'Can change session',6,'change_session'),
	 (23,'Can delete session',6,'delete_session'),
	 (24,'Can view session',6,'view_session'),
	 (25,'Can add Album',7,'add_album'),
	 (26,'Can change Album',7,'change_album'),
	 (27,'Can delete Album',7,'delete_album'),
	 (28,'Can view Album',7,'view_album'),
	 (29,'Can add Album Type',8,'add_albumtype'),
	 (30,'Can change Album Type',8,'change_albumtype');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (31,'Can delete Album Type',8,'delete_albumtype'),
	 (32,'Can view Album Type',8,'view_albumtype'),
	 (33,'Can add Album Link',9,'add_albumlink'),
	 (34,'Can change Album Link',9,'change_albumlink'),
	 (35,'Can delete Album Link',9,'delete_albumlink'),
	 (36,'Can view Album Link',9,'view_albumlink'),
	 (37,'Can add Artist',10,'add_artist'),
	 (38,'Can change Artist',10,'change_artist'),
	 (39,'Can delete Artist',10,'delete_artist'),
	 (40,'Can view Artist',10,'view_artist');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (41,'Can add Artist Link',11,'add_artistlink'),
	 (42,'Can change Artist Link',11,'change_artistlink'),
	 (43,'Can delete Artist Link',11,'delete_artistlink'),
	 (44,'Can view Artist Link',11,'view_artistlink'),
	 (45,'Can add Genre',12,'add_genre'),
	 (46,'Can change Genre',12,'change_genre'),
	 (47,'Can delete Genre',12,'delete_genre'),
	 (48,'Can view Genre',12,'view_genre'),
	 (49,'Can add Music Group',13,'add_musicgroup'),
	 (50,'Can change Music Group',13,'change_musicgroup');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (51,'Can delete Music Group',13,'delete_musicgroup'),
	 (52,'Can view Music Group',13,'view_musicgroup'),
	 (53,'Can add Playlist',14,'add_playlist'),
	 (54,'Can change Playlist',14,'change_playlist'),
	 (55,'Can delete Playlist',14,'delete_playlist'),
	 (56,'Can view Playlist',14,'view_playlist'),
	 (57,'Can add Song-Playlist Relation',15,'add_songplaylistrelation'),
	 (58,'Can change Song-Playlist Relation',15,'change_songplaylistrelation'),
	 (59,'Can delete Song-Playlist Relation',15,'delete_songplaylistrelation'),
	 (60,'Can view Song-Playlist Relation',15,'view_songplaylistrelation');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (61,'Can add Pending Song',16,'add_pendingsong'),
	 (62,'Can change Pending Song',16,'change_pendingsong'),
	 (63,'Can delete Pending Song',16,'delete_pendingsong'),
	 (64,'Can view Pending Song',16,'view_pendingsong'),
	 (65,'Can add Song',17,'add_song'),
	 (66,'Can change Song',17,'change_song'),
	 (67,'Can delete Song',17,'delete_song'),
	 (68,'Can view Song',17,'view_song'),
	 (69,'Can add Task',18,'add_task'),
	 (70,'Can change Task',18,'change_task');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (71,'Can delete Task',18,'delete_task'),
	 (72,'Can view Task',18,'view_task'),
	 (73,'Can add Task Comment',19,'add_taskcomment'),
	 (74,'Can change Task Comment',19,'change_taskcomment'),
	 (75,'Can delete Task Comment',19,'delete_taskcomment'),
	 (76,'Can view Task Comment',19,'view_taskcomment'),
	 (77,'Can add Audit Log',20,'add_auditlog'),
	 (78,'Can change Audit Log',20,'change_auditlog'),
	 (79,'Can delete Audit Log',20,'delete_auditlog'),
	 (80,'Can view Audit Log',20,'view_auditlog');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (81,'Can add Songs Link',21,'add_songlink'),
	 (82,'Can change Songs Link',21,'change_songlink'),
	 (83,'Can delete Songs Link',21,'delete_songlink'),
	 (84,'Can view Songs Link',21,'view_songlink'),
	 (85,'Can add Missing Data from Artists',22,'add_missingdataartist'),
	 (86,'Can change Missing Data from Artists',22,'change_missingdataartist'),
	 (87,'Can delete Missing Data from Artists',22,'delete_missingdataartist'),
	 (88,'Can view Missing Data from Artists',22,'view_missingdataartist'),
	 (89,'Can add Z_Missing Data: Albums',23,'add_missingdataalbum'),
	 (90,'Can change Z_Missing Data: Albums',23,'change_missingdataalbum');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (91,'Can delete Z_Missing Data: Albums',23,'delete_missingdataalbum'),
	 (92,'Can view Z_Missing Data: Albums',23,'view_missingdataalbum'),
	 (93,'Can add Z_Missing Data: Albums Links',24,'add_missingdataalbumlink'),
	 (94,'Can change Z_Missing Data: Albums Links',24,'change_missingdataalbumlink'),
	 (95,'Can delete Z_Missing Data: Albums Links',24,'delete_missingdataalbumlink'),
	 (96,'Can view Z_Missing Data: Albums Links',24,'view_missingdataalbumlink'),
	 (97,'Can add Z_Missing Data: Artists Links',25,'add_missingdataartistlink'),
	 (98,'Can change Z_Missing Data: Artists Links',25,'change_missingdataartistlink'),
	 (99,'Can delete Z_Missing Data: Artists Links',25,'delete_missingdataartistlink'),
	 (100,'Can view Z_Missing Data: Artists Links',25,'view_missingdataartistlink');
INSERT INTO public.auth_permission (id,"name",content_type_id,codename) VALUES
	 (101,'Can add Z_Missing Data: Songs',26,'add_missingdatasong'),
	 (102,'Can change Z_Missing Data: Songs',26,'change_missingdatasong'),
	 (103,'Can delete Z_Missing Data: Songs',26,'delete_missingdatasong'),
	 (104,'Can view Z_Missing Data: Songs',26,'view_missingdatasong'),
	 (105,'Can add Z_Missing Data: Songs Links',27,'add_missingdatasonglink'),
	 (106,'Can change Z_Missing Data: Songs Links',27,'change_missingdatasonglink'),
	 (107,'Can delete Z_Missing Data: Songs Links',27,'delete_missingdatasonglink'),
	 (108,'Can view Z_Missing Data: Songs Links',27,'view_missingdatasonglink');

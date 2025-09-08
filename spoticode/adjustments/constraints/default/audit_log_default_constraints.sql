CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE audit_log ALTER COLUMN id SET DEFAULT uuid_generate_v4();
ALTER TABLE audit_log ALTER COLUMN user SET DEFAULT def_fn_get_deleted_user();
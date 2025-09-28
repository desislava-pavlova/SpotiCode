import threading

_local = threading.local()


def set_current_db(alias):
    _local.db = alias

def get_current_db():
    return getattr(_local, "db", "default")


class UserDBRouter:
    DEFAULT_APPS = ("auth", "sessions", "contenttypes", "admin", "messages")
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return "default"
        return get_current_db()

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.DEFAULT_APPS:
            return "default"
        return get_current_db()

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.DEFAULT_APPS:
            return "default"
        return db != "default"

from django.apps import AppConfig


class AuditlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spoticode.auditlog'

    def ready(self):
        import spoticode.auditlog.signals
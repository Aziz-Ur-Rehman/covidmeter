from django.apps import AppConfig


class CovidConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = "covid"
    name = "api.covid"

    def ready(self):
        import api.covid.signals

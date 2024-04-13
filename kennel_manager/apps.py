from django.apps import AppConfig


class KennelManagerConfig(AppConfig):
    """
    AppConfig for the Kennel Manager app.

    This class defines the configuration for the Kennel Manager app,
    including the default auto field and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kennel_manager'

from django.apps import AppConfig
from django.contrib.auth import get_user_model

class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'

    def ready(self):
    	from payments import signals
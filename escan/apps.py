# from django.apps import AppConfig


# class EscanConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'escan'

#     def ready(self):
#         import escan.signals


# apps.py
from django.apps import AppConfig

class EscanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escan'

    def ready(self):
        # DO NOT LOAD TORCH HERE
        pass

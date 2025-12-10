# from django.apps import AppConfig


# class EscanConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'escan'

#     def ready(self):
#         import escan.signals


from django.apps import AppConfig
import torch
from .views import load_disease_model, load_variety_model  # import both

class EscanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escan'

    def ready(self):
        global disease_model
        disease_model = load_disease_model()  # load once

        global variety_model
        variety_model = load_variety_model()  # load once

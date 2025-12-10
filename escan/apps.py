# from django.apps import AppConfig


# class EscanConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'escan'

#     def ready(self):
#         import escan.signals


from django.apps import AppConfig

class EscanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escan'

    def ready(self):
        import torch
        from .model_loaders import load_disease_model, load_variety_model

        # store on the AppConfig instance
        self.disease_model = load_disease_model()
        self.variety_model = load_variety_model()

# model_loaders.py
import functools
import torch
import torchvision.models as models


@functools.lru_cache(maxsize=1)
def load_variety_model():
    model = models.resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 9)
    model.load_state_dict(torch.load('escan/model/banana_variety_resnet_state_dict.pth',
                                     map_location='cpu'))
    model.eval()
    return model


@functools.lru_cache(maxsize=1)
def load_disease_model():
    model = models.resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 11)
    model.load_state_dict(torch.load(
        'escan/model/banana_disease(F)_resnet_state_dict.pth',
        map_location='cpu'
    ))
    model.eval()
    return model

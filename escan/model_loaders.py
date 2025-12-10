import torch
import torchvision.models as models

def load_variety_model():
    # Load the variety model (Replace with your actual model loading code)
    model = models.resnet18(weights=None)  # Example, change to your model
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 9)  # number of classes in your variety model
    model.load_state_dict(torch.load('escan/model/banana_variety_resnet_state_dict.pth'))
    model.eval()
    return model


def load_disease_model():
    # Load the disease model
    model = models.resnet18(weights=None)  # Replace with your actual model if not ResNet18
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, 11)  # 11 classes for disease
    # Load state dict
    model.load_state_dict(
        torch.load('escan/model/banana_disease(F)_resnet_state_dict.pth', map_location='cpu')
    )
    model.eval()
    return model

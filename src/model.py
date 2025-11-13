import torch.nn as nn
from torchvision import models

class DeepfakeDetector(nn.Module):
    def __init__(self):
        super().__init__()
        self.base = models.efficientnet_b0(weights="IMAGENET1K_V1")
        self.base.features[0][0] = nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1)
        self.classifier = nn.Linear(1000, 2)

    def forward(self, x):
        x = self.base(x)
        x = self.classifier(x)
        return x

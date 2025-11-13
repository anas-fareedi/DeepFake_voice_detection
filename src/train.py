import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from dataset import MelDataset
from model import DeepfakeDetector

train_ds = MelDataset("processed")
train_dl = DataLoader(train_ds, batch_size=16, shuffle=True)

model = DeepfakeDetector()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=2e-4)

for epoch in range(10):
    for mel, label in train_dl:
        optimizer.zero_grad()
        pred = model(mel)
        loss = criterion(pred, label)
        loss.backward()
        optimizer.step()
    print("Epoch", epoch, "Loss:", loss.item())

torch.save(model.state_dict(), "models/deepfake_detector.pth")

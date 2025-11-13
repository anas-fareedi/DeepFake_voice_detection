import torch
from torch.utils.data import Dataset
import numpy as np
import os

class MelDataset(Dataset):
    def __init__(self, root):
        self.paths = []
        self.labels = []
        for label, cls in enumerate(["real", "fake"]):
            for file in os.listdir(f"{root}/{cls}"):
                self.paths.append(f"{root}/{cls}/{file}")
                self.labels.append(label)
    
    def __getitem__(self, idx):
        mel = np.load(self.paths[idx])
        
        # mel = torch.tensor(mel).unsqueeze(0).float()
        mel = torch.from_numpy(np.asarray(mel, dtype=np.float32)).unsqueeze(0)

        label = torch.tensor(self.labels[idx]).long()
        return mel, label

    def __len__(self):
        return len(self.paths)

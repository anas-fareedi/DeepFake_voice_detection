import torch
import numpy as np
import librosa
from model import DeepfakeDetector
import sys

model_path = "models/deepfake_detector.pth"
model = DeepfakeDetector()
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

# ----- Convert audio to mel spectrogram -----
def audio_to_mel(path):
    y, sr = librosa.load(path, sr=16000)
    y = librosa.util.fix_length(data=y, size=16000 * 3)

    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    mel_db = librosa.power_to_db(mel, ref=np.max)

    mel_db = np.asarray(mel_db, dtype=np.float32)
    mel_db = torch.from_numpy(mel_db).unsqueeze(0).unsqueeze(0)  
    return mel_db

# ----- Prediction function -----
def predict(audio_path):
    mel = audio_to_mel(audio_path)
    with torch.no_grad():
        output = model(mel)
        probs = torch.softmax(output, dim=1)
        confidence, cls = torch.max(probs, dim=1)

        label = "REAL" if cls.item() == 0 else "FAKE"

        return label, round(confidence.item() * 100, 2)

# ----- CLI -----
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    label, conf = predict(audio_file)

    print(f"\nPrediction: {label}  (confidence: {conf}%)\n")
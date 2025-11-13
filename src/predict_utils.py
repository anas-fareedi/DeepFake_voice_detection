import torch
import numpy as np
import librosa
from src.model import DeepfakeDetector
import io
# Load model once
model_path = "./models/deepfake_detector.pth"
model = DeepfakeDetector()
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()

def preprocess_audio(file_bytes):
    audio_stream = io.BytesIO(file_bytes)
    # Load from bytes
    y, sr = librosa.load(audio_stream, sr=16000)

    # Fix length to 3 seconds
    y = librosa.util.fix_length(data=y, size=16000 * 3)

    # Convert to mel spectrogram
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    mel_db = librosa.power_to_db(mel, ref=np.max)

    mel_db = np.asarray(mel_db, dtype=np.float32)

    mel_tensor = torch.from_numpy(mel_db).unsqueeze(0).unsqueeze(0)
    return mel_tensor

def predict_from_audio(file_bytes):
    mel = preprocess_audio(file_bytes)

    with torch.no_grad():
        output = model(mel)
        probs = torch.softmax(output, dim=1)
        confidence, cls = torch.max(probs, dim=1)

    label = "REAL" if cls.item() == 0 else "FAKE"
    return label, round(confidence.item() * 100, 2)

# import torch
# import numpy as np
# import librosa
# from src.model import DeepfakeDetector
# import io
# # Load model once
# model_path = "./models/deepfake_detector.pth"
# model = DeepfakeDetector()
# model.load_state_dict(torch.load(model_path, map_location="cpu"))
# model.eval()

# def preprocess_audio(file_bytes):
#     audio_stream = io.BytesIO(file_bytes)
#     # Load from bytes
#     y, sr = librosa.load(audio_stream, sr=16000)

#     # Fix length to 3 seconds
#     y = librosa.util.fix_length(data=y, size=16000 * 3)

#     # Convert to mel spectrogram
#     mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
#     mel_db = librosa.power_to_db(mel, ref=np.max)

#     mel_db = np.asarray(mel_db, dtype=np.float32)

#     mel_tensor = torch.from_numpy(mel_db).unsqueeze(0).unsqueeze(0)
#     return mel_tensor

# def predict_from_audio(file_bytes):
#     mel = preprocess_audio(file_bytes)

#     with torch.no_grad():
#         output = model(mel)
#         probs = torch.softmax(output, dim=1)
#         confidence, cls = torch.max(probs, dim=1)

#     label = "REAL" if cls.item() == 0 else "FAKE"
#     return label, round(confidence.item() * 100, 2)

import torch
import numpy as np
import librosa
import io
import os
import subprocess
import tempfile
import soundfile as sf
from src.model import DeepfakeDetector


# -----------------------------
# MODEL LOADING (Docker-safe)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "models", "deepfake_detector.pth")
model_path = os.path.normpath(model_path)

model = DeepfakeDetector()
model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()


# -----------------------------
# AUDIO DECODER (WEBM → WAV)
# -----------------------------
def decode_audio_to_wav(file_bytes):
    """Converts WebM/MP3/M4A/anything → WAV using ffmpeg."""

    # Save incoming blob to a temp .webm file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp_in:
        tmp_in.write(file_bytes)
        tmp_in.flush()

        # Output WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_out:
            command = [
                "ffmpeg",
                "-y",
                "-i", tmp_in.name,   # input
                "-ar", "16000",       # sample rate
                "-ac", "1",           # mono
                tmp_out.name          # output
            ]

            subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            # Load WAV using soundfile
            data, sr = sf.read(tmp_out.name)

            # Convert stereo → mono
            if len(data.shape) > 1:
                data = np.mean(data, axis=1)

            return data.astype(np.float32), sr


# -----------------------------
# PREPROCESSING PIPELINE
# -----------------------------
def preprocess_audio(file_bytes):
    # Decode ANY format to WAV first
    y, sr = decode_audio_to_wav(file_bytes)

    # Ensure 3 seconds of audio
    # y = librosa.util.fix_length(y, 16000 * 3)
    # Ensure 3 seconds of audio

    # new
    y = librosa.util.fix_length(data=y, size=16000 * 3)


    # Mel spectrogram
    mel = librosa.feature.melspectrogram(
        y=y, sr=16000, n_mels=128
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)

    mel_db = mel_db.astype(np.float32)
    mel_tensor = torch.from_numpy(mel_db).unsqueeze(0).unsqueeze(0)

    return mel_tensor


# -----------------------------
# PREDICTION PIPELINE
# -----------------------------
def predict_from_audio(file_bytes):
    mel = preprocess_audio(file_bytes)

    with torch.no_grad():
        output = model(mel)
        probs = torch.softmax(output, dim=1)
        confidence, cls = torch.max(probs, dim=1)

    label = "REAL" if cls.item() == 0 else "FAKE"
    return label, round(confidence.item() * 100, 2)

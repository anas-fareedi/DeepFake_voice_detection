import librosa
import numpy as np
import os

def audio_to_mel(path):
    y, sr = librosa.load(path, sr=16000)
    y = librosa.util.fix_length(data=y, size=16000 * 3)  # fixed 3 sec
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return mel_db

output_dir = "processed"

os.makedirs(output_dir, exist_ok=True)

for cls in ["real", "fake"]:
    os.makedirs(f"{output_dir}/{cls}", exist_ok=True)
    for file in os.listdir(f"data/{cls}"):
        mel = audio_to_mel(f"data/{cls}/{file}")
        np.save(f"{output_dir}/{cls}/{file}.npy", mel)

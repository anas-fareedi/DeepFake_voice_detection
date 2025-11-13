import librosa
import soundfile as sf
import os

input_dir = "data_raw"
output_dir = "data"

os.makedirs(output_dir, exist_ok=True)

TARGET_SR = 16000

for cls in ["real", "fake"]:
    os.makedirs(f"{output_dir}/{cls}", exist_ok=True)
    for file in os.listdir(f"{input_dir}/{cls}"):
        path = f"{input_dir}/{cls}/{file}"
        audio, sr = librosa.load(path, sr=TARGET_SR, mono=True)
        sf.write(f"{output_dir}/{cls}/{file}", audio, TARGET_SR)

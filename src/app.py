from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.predict_utils import predict_from_audio

app = FastAPI()

# Enable CORS for your JS frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://voice-sentinel-scan.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],       
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Deepfake Voice Detection API Running"}

@app.post("/predict")
async def predict_audio(file: UploadFile = File(...)):
    file_bytes = await file.read()

    label, confidence = predict_from_audio(file_bytes)
    
    return {
        "prediction": label,
        "confidence": confidence
    }
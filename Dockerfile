FROM python:3.10-slim

WORKDIR /app

# System dependencies for librosa + soundfile
RUN apt-get update && apt-get install -y \
    libsndfile1 ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

# Install all Python packages (Torch CPU)
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY . .

# Run FastAPI on port 10000 (Render requirement)
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "10000"]
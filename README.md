# DeepFake_voice_detection

Make this impactful project by overseeing the current scenario related to ai generated voice fraud 

Frontend_URL : https://voicesentinel.anasfareedi.in/

Backend_URL : https://deepfake-voice-detection-1.onrender.com/


------
Badges
- CI: [![CI](https://img.shields.io/badge/ci-pending-lightgrey)]()
- License: [![License](https://img.shields.io/badge/license-MIT-blue)]()
- Coverage: [![Coverage](https://img.shields.io/badge/coverage-0%25-lightgrey)]()

Table of contents
- [About](#about)
- [Features](#features)
- [Tech stack](#tech-stack)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Development](#development)
- [Testing](#testing)
- [Release / CI](#release--ci)
- [Contributing](#contributing)
- [License](#license)
- [Maintainers & Support](#maintainers--support)


<img width="1647" height="877" alt="image" src="https://github.com/user-attachments/assets/54b1a8d9-2850-43d3-a82a-34578c02e73d" />

About
-----

**DeepFake Voice Detection** is an AI-powered solution designed to combat the growing threat of AI-generated voice fraud and deepfake audio scams. As synthetic voice technology becomes increasingly sophisticated and accessible, malicious actors can impersonate individuals with alarming accuracy, leading to fraud, misinformation, and identity theft.

This project leverages deep learning and audio signal processing to detect whether a given voice recording is authentic or AI-generated. Built with a CNN-based architecture using EfficientNet-B0 and mel-spectrogram analysis, the system achieves reliable classification of real vs. fake audio samples.

The solution includes:
- A **FastAPI backend** for audio processing and inference
- A **web frontend** ([Voice Sentinel Scan](https://voice-sentinel-scan.vercel.app/)) for easy audio upload and analysis
- Docker support for streamlined deployment
- Pre-trained model for immediate detection capability

**Use cases:**
- Verifying authenticity of voice messages and recordings
- Protecting against phone scam attacks using voice cloning
- Media forensics and fact-checking
- Authentication systems requiring voice verification
- Organizational security against social engineering attacks

Features
--------

### Core Detection Capabilities
- **Real-time Audio Analysis**: Upload audio files in multiple formats (WAV, MP3, WebM, M4A) and receive instant deepfake predictions
- **High-Accuracy Classification**: CNN-based model trained on mel-spectrogram features to distinguish real from synthetic voices
- **Confidence Scoring**: Provides percentage-based confidence levels alongside binary REAL/FAKE predictions

### Audio Processing Pipeline
- **Multi-format Support**: Automatic audio decoding using FFmpeg to handle various input formats
- **Standardized Preprocessing**: Converts all audio to 16kHz mono for consistent analysis
- **Mel-Spectrogram Extraction**: Generates 128-band mel-spectrograms for feature representation
- **Fixed-length Processing**: Normalizes audio clips to 3-second segments for model input

### Machine Learning Architecture
- **EfficientNet-B0 Backbone**: Transfer learning from ImageNet for robust feature extraction from spectrograms
- **Custom Binary Classifier**: Fine-tuned final layers for deepfake detection task
- **PyTorch Framework**: Built on industry-standard deep learning library for flexibility and performance

### API & Integration
- **RESTful FastAPI Endpoint**: `/predict` endpoint accepts audio uploads and returns JSON predictions
- **CORS Enabled**: Ready for frontend integration from any origin
- **Lightweight Inference**: CPU-optimized model loading for cost-effective deployment
- **Docker Containerization**: Pre-configured Dockerfile for easy deployment to cloud platforms

### Development Tools
- **Training Pipeline**: Complete scripts for dataset preprocessing, mel-spectrogram generation, and model training
- **Modular Architecture**: Separated components for preprocessing, training, and inference
- **CLI Prediction Tool**: Command-line interface for batch processing and testing
- **Test Audio Samples**: Included test cases for validation

### Production Ready
- **Web Interface**: User-friendly frontend deployed at [voice-sentinel-scan.vercel.app](https://voice-sentinel-scan.vercel.app/)
- **Scalable Backend**: FastAPI ensures high-performance concurrent request handling
- **Environment Flexibility**: Configurable for local development or cloud deployment

Tech stack
----------
List the primary languages, frameworks, and major libraries used:
- Language: Python
- Libraries : Librosa , Pytorch 
- Web framework :  FastAPI
- Other: Docker

Requirements
------------
- Git >= 2.0
- Docker (optional, if Docker support provided)
- Any other system dependencies or tools

Quick start
-----------
Clone the repository and run the most common setup steps.

git clone https://github.com/<owner>/<repo>.git
cd <repo>

Install dependencies (pick the one that matches the project):

Node (npm)
npm install
npm run build
npm start

Yarn
yarn
yarn build
yarn start

Python (venv + pip)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m <your_package>.main

Go
go build ./...
./<binary>

Docker
docker build -t <repo>:latest .
docker run -p 8080:8080 -e ENV_VAR=value <repo>:latest

Usage
-----
Explain how to run or use the project after installation. Include one or two real examples.

- Run locally:
  npm run dev
  OR
  python -m <your_package>

- Example API request (if applicable):
  curl -X POST http://localhost:8080/api/v1/resource \
    -H "Content-Type: application/json" \
    -d '{"key":"value"}'

Configuration
-------------
List important environment variables, config files, or flags. Provide defaults where sensible.

ENV_VAR_NAME=default-value
DATABASE_URL=postgres://user:pass@localhost:5432/dbname
PORT=8080

Store sensitive values in a .env file (do not commit .env to git).

Development
-----------
Describe common developer workflows and helpful commands:

- Create a feature branch:
  git checkout -b feat/short-description

- Run linters and formatters:
  npm run lint
  npm run format

- Run the app in watch mode:
  npm run dev
  OR
  air (for Go), nodemon, etc.

Testing
-------
Briefly document how to run tests and any important testing guidelines.

- Run unit tests:
  npm test
  OR
  pytest
  OR
  go test ./...

- Run coverage:
  npm run coverage
  OR
  pytest --cov=your_package

Release / CI
-------------
Describe how CI and releases work (link to workflow files if present). Example:

We use GitHub Actions for CI. Pushing to main triggers tests and builds; creating a release uses semantic versioning and produces artifacts.

Contributing
------------
If you welcome contributions, add brief rules and point to CONTRIBUTING.md:

- Read CONTRIBUTING.md before opening issues or PRs.
- Open a descriptive issue first for non-trivial changes.
- Create small PRs with clear explanations and tests where applicable.

Code of conduct
---------------
By participating, you agree to abide by the Code of Conduct in CODE_OF_CONDUCT.md.

License
-------
This project is licensed under the MIT License — see the LICENSE file for details.

Maintainers & Support
---------------------
Maintainer(s): anas-fareedi
For questions or help, open an issue or contact the maintainers.

Appendix / Useful links
-----------------------
- Architecture doc: docs/ARCHITECTURE.md (if present)
- API reference: docs/API.md or /docs swagger
- Roadmap: docs/ROADMAP.md

Replace placeholders (<owner>, <repo>, <your_package>, etc.) with repository-specific values. If you want, I can generate a customized README with concrete commands and examples if you tell me:
- primary language / framework,
- how to install & run the project,
- one or two example commands or endpoints,
- license,
- any CI or Docker specifics.

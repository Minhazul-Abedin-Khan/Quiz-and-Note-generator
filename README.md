# Quiz and Note Generator

AI-powered application that generates note summaries, audio transcriptions, and customized quizzes from images using Google's Gemini API.

**Deployment:** https://quiz-and-note-generator.streamlit.app/

## Features

- Image note processing (up to 3 images)
- AI-powered note summarization
- Audio transcription
- Quiz generation (Easy, Medium, Hard difficulty)

## Tech Stack

- Streamlit
- Google Gemini API
- Pillow
- gTTS
- python-dotenv

## Requirements

- Python 3.8+
- Google Gemini API key

## Installation

```bash
git clone <repository-url>
cd "Project using GEMINI and Streamlit"
python -m venv project1venv
source project1venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
```

Run:
```bash
streamlit run app.py
```

## Usage

1. Upload images of notes
2. Select quiz difficulty
3. Click "Click the button to initiate AI"
4. View results (notes, audio, quiz)

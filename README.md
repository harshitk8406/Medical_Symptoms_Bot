# 🩺 Medical Symptoms Bot

An AI-powered symptom checker that gives users a plain-language explanation of possible causes for their symptoms — powered by Groq's LLM API, with a fast FastAPI backend and a React chat-style frontend.

> ⚠️ **Disclaimer:** This tool is for informational purposes only and is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for any medical concerns.

---

## Overview

Users type in their symptoms through a chat-like interface, pick an LLM model, and get an AI-generated, plain-language explanation of possible causes — along with a reminder to consult a doctor. The frontend mimics a chatbot experience with autocomplete suggestions, a typing animation for responses, persistent chat history, and dark mode.

---

## Features

- **AI Symptom Analysis** — Describes possible causes for user-reported symptoms using Groq-hosted LLMs
- **Multiple Model Selection** — Switch between Llama 3.1 8B (fast), Llama 3.3 70B (powerful), Llama 4 Scout 17B, and Qwen3 32B
- **Smart Autocomplete** — Type-ahead symptom suggestions with keyboard navigation (arrow keys + Enter)
- **Chat-Style UI** — Conversational interface with a typing animation for bot responses
- **Persistent History** — Chat history and dark mode preference saved locally via `localStorage`
- **Dark Mode** — Toggleable light/dark theme
- **Single-Origin Deployment** — FastAPI serves the built React app directly in production

---

## Tech Stack

| Layer      | Technology                          |
| ---------- | ------------------------------------ |
| Frontend   | React 19, Axios, CSS                 |
| Backend    | FastAPI, Uvicorn, Pydantic           |
| AI         | Groq API (Llama 3.1/3.3/4, Qwen3)    |
| Config     | python-dotenv                        |

---

## Project Structure

```
Medical_Symptoms_Bot/
├── backend/
│   ├── main.py            # FastAPI app, /analyze endpoint, Groq integration
│   ├── requirements.txt   # Python dependencies
│   └── .env.example       # Environment variable template
├── frontend/
│   ├── src/
│   │   ├── App.js             # Root component
│   │   ├── SymptomForm.js     # Main chat UI, state, and API calls
│   │   ├── Api.js             # Axios API client
│   │   └── Symptoms.js        # Autocomplete symptom suggestions
│   └── public/
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- A [Groq API key](https://console.groq.com)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# then edit .env and add your GROQ_API_KEY

uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The app will be available at `http://localhost:3000`.

### Environment Variables

Create a `.env` file inside the `backend/` directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## API Reference

### `POST /analyze`

Analyzes user-described symptoms and returns an AI-generated explanation.

**Request body:**

```json
{
  "symptoms": "sore throat, fever, headache",
  "model": "llama-3.1-8b-instant"
}
```

**Response:**

```json
{
  "response": "Plain-language explanation of possible causes..."
}
```

---

## Production Build

Build the React frontend and let FastAPI serve it directly:

```bash
cd frontend
npm run build
cd ../backend
uvicorn main:app
```

FastAPI automatically mounts and serves `frontend/build` when the folder is present.

---

## Roadmap / Potential Improvements

- [ ] Add authentication and per-user chat history
- [ ] Persist chat history server-side instead of `localStorage`
- [ ] Add symptom severity triage / urgency flags
- [ ] Rate limiting on the `/analyze` endpoint
- [ ] Deploy live demo

---

## License

This project is open source. Feel free to use and modify it.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class SymptomInput(BaseModel):
    symptoms: str
    model: str = 'llama-3.1-8b-instant'

@app.post('/analyze')
def analyze(symptoms: SymptomInput):
    prompt = (
        f'You are a very helpful medical assistant. A user described their symptoms as: '
        f'\'{symptoms.symptoms}\'.\n\n'
        f'Provide a plain-language explanation of possible causes, but remind them to consult a doctor.'
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=symptoms.model,
        )
        output = chat_completion.choices[0].message.content
        return {'response': output.strip()}
    except Exception as e:
        return {'error': str(e)}

# Serve React frontend (built static files)
build_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend", "build")

if os.path.exists(build_path):
    app.mount("/static", StaticFiles(directory=os.path.join(build_path, "static")), name="static-assets")

    @app.get("/{full_path:path}")
    def serve_react(full_path: str):
        return FileResponse(os.path.join(build_path, "index.html"))
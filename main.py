from fastapi import FastAPI
from google import genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Insta Notes Backend")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

client = genai.Client(api_key=api_key)

class GenerateNoteRequest(BaseModel):
    videoUrl: str

@app.get("/")
def root():
    return {"message": "Backend working"}

@app.post("/generate-notes")
async def generate_notes(request: GenerateNoteRequest):
    try:
        prompt = f"Generate clear study notes from this YouTube video: {request.videoUrl}"

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return {
            "success": True,
            "notes": response.text
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "Wedding AI Backend Running"}

"/chat"
def chat(req: ChatRequest):
    response = client.responses.create(
        model="gpt-5-mini",
        input=req.message
    )

    return {
        "answer": response.output_text
    }

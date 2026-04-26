import os
from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Read API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Emotional Support AI")

# Simple request model
class ChatRequest(BaseModel):
    message: str
    history: List[Dict] = []

@app.post("/api/chat")
def chat(req: ChatRequest):
    # System prompt: make the assistant empathetic and safe
    system_prompt = (
        "You are a compassionate, non-judgmental emotional support assistant. "
        "Provide empathetic responses, validate feelings, offer coping strategies, "
        "and include a safety disclaimer. If the user says they are in immediate danger or "
        "talks about self-harm, encourage them to seek immediate help and provide crisis resources."
    )                                                                                                                                                                                                                                                                                                                        MM
    

    # Build message list for ChatCompletion
    messages = [{"role": "system", "content": system_prompt}]
    # history is expected as list of {"role": "user"|"assistant", "content": "..."}
    for h in req.history:
        messages.append(h)
    messages.append({"role": "user", "content": req.message})

    # Call OpenAI ChatCompletion (example with gpt-3.5-turbo)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
        n=1,
    )

    assistant_text = response["choices"][0]["message"]["content"].strip()
    return {"reply": assistant_text}
    from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="static")

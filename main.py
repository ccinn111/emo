import os
from typing import List, Dict
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Emotional Support AI")

class ChatRequest(BaseModel):
    message: str
    history: List[Dict] = []

@app.post("/api/chat")
def chat(req: ChatRequest):
    system_prompt = (
        "You are a compassionate, non-judgmental emotional support assistant. "
        "Provide empathetic responses, validate feelings, offer coping strategies, "
        "and include a safety disclaimer. If the user says they are in immediate danger or "
        "talks about self-harm, encourage them to seek immediate help and provide crisis resources."
    )
    messages = [{"role": "system", "content": system_prompt}]
    for h in req.history:
        messages.append(h)
    messages.append({"role": "user", "content": req.message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
        n=1,
    )
    assistant_text = response["choices"][0]["message"]["content"].strip()
    return {"reply": assistant_text}

# 静态文件服务（必须放在所有 API 路由之后）
app.mount("/", StaticFiles(directory="static", html=True), name="static")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Middleware CORS – bardzo ważne, że PRZED wszystkim innym
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model zapytania
class Question(BaseModel):
    question: str

# 🛠️ Ręczna obsługa preflight request (OPTIONS)
@app.options("/ask")
async def options_ask():
    return {}

# Endpoint główny
@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Otrzymałem: {q.question}"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔓 CORS Middleware
origins = [
    "https://lukaszlub.github.io",
    "https://lukaszlub.github.io/chatbot-trasti-frontend",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Endpoint zdrowia (dla Render + dla testów)
@app.get("/")
async def root():
    return {"message": "Chatbot backend działa"}

# ✅ Endpoint CORS preflight (nie zawsze potrzebny, ale bywa pomocny)
@app.options("/ask")
async def options_ask():
    return {}

# 🔹 Model zapytania
class Question(BaseModel):
    question: str

# 🔹 Endpoint bota
@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Otrzymałem: {q.question}"}

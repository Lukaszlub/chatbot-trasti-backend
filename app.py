from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# ✅ Poprawna domena frontendowa
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io", "https://lukaszlub.github.io/chatbot-trasti-frontend/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

# ✅ Obsługa preflight (CORS - OPTIONS)
@app.options("/ask")
async def options_handler():
    return JSONResponse(status_code=200)

# 🔹 Główna logika
@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Otrzymałem: {q.question}"}

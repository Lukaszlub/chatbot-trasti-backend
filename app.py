from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔓 Zezwalamy tylko na ruch z GitHub Pages (lub inną stronę frontendową)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io"],  # Twój frontend
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Model danych przychodzących z frontu
class Question(BaseModel):
    question: str

# 🔹 Przykładowa logika odpowiedzi (zamień na integrację z LangChain/OpenAI)
@app.post("/ask")
async def ask(q: Question):
    user_question = q.question.strip()
    if not user_question:
        return {"answer": "Nie otrzymałem pytania."}
    
    # Tutaj możesz użyć LangChain / OpenAI / Chroma itp.
    return {"answer": f"🔁 Otrzymałem pytanie: {user_question}"}

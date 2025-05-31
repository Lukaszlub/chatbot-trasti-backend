from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔓 Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io"],  # <- adres Twojej strony
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Model pytania
class Question(BaseModel):
    question: str

# 🔁 Opcjonalnie: obsługa zapytań OPTIONS ręcznie
@app.options("/ask")
async def preflight():
    return {}

# 🔹 Główna logika bota (zastąp integracją z OpenAI/LangChain)
@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Odpowiedź na pytanie: {q.question}"}

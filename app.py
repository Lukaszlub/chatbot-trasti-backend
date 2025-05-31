from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔓 Middleware CORS — pozwala na połączenia np. z GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub ["https://lukaszlub.github.io"] dla większego bezpieczeństwa
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Model zapytania
class Question(BaseModel):
    question: str

# 🔹 Przykładowy endpoint
@app.post("/ask")
async def ask(q: Question):
    # Tutaj możesz wstawić integrację z LangChain / OpenAI / bazą wektorową
    return {"answer": f"Otrzymałem: {q.question}"}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# ✅ CORS poprawnie skonfigurowany
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Model zapytania
class Question(BaseModel):
    question: str

# ✅ Obsługa preflight request (OPTIONS), aby uniknąć błędu 404
@app.options("/ask")
async def preflight():
    return JSONResponse(content={"message": "CORS preflight ok"}, status_code=200)

# 🔹 Główna logika
@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Otrzymałem: {q.question}"}

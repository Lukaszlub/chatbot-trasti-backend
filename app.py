from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔓 Middleware CORS — pozwala na połączenia np. z GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lukaszlub.github.io"],  # lub ["https://lukaszlub.github.io"] dla większego bezpieczeństwa
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Model zapytania
class Question(BaseModel):
    question: str

# 🔹 Przykładowy endpoint
from fastapi.responses import JSONResponse

@app.options("/ask")
async def options_handler():
    return JSONResponse(status_code=200)

@app.post("/ask")
async def ask(q: Question):
    return {"answer": f"Otrzymałem: {q.question}"}

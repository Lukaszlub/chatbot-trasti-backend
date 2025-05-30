from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedding = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    organization="org-GmqnMo92LiCCNBTFLARvy7o6"
)

vectordb = Chroma(persist_directory="chroma_index", embedding_function=embedding)

qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        model_name="gpt-4",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        organization="org-GmqnMo92LiCCNBTFLARvy7o6"
    ),
    retriever=vectordb.as_retriever()
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(q: Question):
    return {"answer": qa.run(q.question)}
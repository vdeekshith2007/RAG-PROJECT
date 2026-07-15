from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from app.rag import ask_question
from app.upload import upload_pdf


app = FastAPI(
    title="RAG PDF Question Answering System",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG PDF QA API Running 🚀"
    }


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return upload_pdf(file)


@app.post("/ask")
def ask(request: QuestionRequest):

    response = ask_question(
        request.question
    )

    return {
        "question": request.question,
        "response": response
    }
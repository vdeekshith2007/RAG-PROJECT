# RDG-PDF-QA
# 📄 Retrieval-Augmented Generation (RAG) PDF Question Answering System

> An end-to-end Generative AI application that enables users to upload PDF documents and ask natural language questions using **Retrieval-Augmented Generation (RAG)**, **LangChain**, **FAISS**, and **Hugging Face LLMs**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-LLM-yellow?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🌟 Overview

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions in natural language.

Instead of generating answers from general knowledge, the system retrieves the most relevant document sections using **semantic search** and produces **accurate, source-grounded responses** with citations.

The application combines modern Generative AI technologies including **LangChain**, **FAISS**, **Sentence Transformers**, **FastAPI**, **Streamlit**, and **Hugging Face Large Language Models**.

---

# ✨ Features

- 📄 Upload one or multiple PDF documents
- 🔍 Semantic search using FAISS Vector Database
- 🧠 Sentence Transformer Embeddings
- 🤖 Hugging Face LLM Integration
- 💬 Retrieval-Augmented Generation (RAG)
- 📚 Source citations with page numbers
- 📑 Incremental PDF indexing
- ⚡ FastAPI REST API
- 🎨 Streamlit Frontend
- 🐳 Docker Support
- ⚙️ Configurable architecture
- 🚀 Production-ready project structure

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
             Upload PDF Document
                      │
                      ▼
                PyPDFLoader
                      │
                      ▼
     Recursive Character Splitter
                      │
                      ▼
      Sentence Transformer Embeddings
                      │
                      ▼
          FAISS Vector Database
                      │
                      ▼
               User Question
                      │
                      ▼
            Similarity Search (Top-K)
                      │
                      ▼
             LangChain RAG Pipeline
                      │
                      ▼
          Hugging Face LLM Generation
                      │
                      ▼
        AI Answer + Source Citations
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| AI Framework | LangChain |
| LLM | Hugging Face Inference API |
| Embeddings | Sentence Transformers |
| Vector Store | FAISS |
| PDF Loader | PyPDFLoader |
| Containerization | Docker |
| API Testing | Swagger UI |

---

# 📂 Project Structure

```text
RAG-PDF-QA
│
├── app
│   ├── config.py
│   ├── create_vectorstore.py
│   ├── ingest.py
│   ├── main.py
│   ├── rag.py
│   └── upload.py
│
├── uploads/
├── vectorstore/
├── data/
│
├── frontend.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/RAG-PDF-QA.git

cd RAG-PDF-QA
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment

Create a `.env` file.

```env
HF_TOKEN=your_huggingface_token
```

---

# ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🎨 Run Streamlit

```bash
streamlit run frontend.py
```

Frontend

```
http://localhost:8501
```

---

# 🐳 Docker

Build Image

```bash
docker build -t rag-pdf-qa .
```

Run Container

```bash
docker run -p 8000:8000 rag-pdf-qa
```

---

# 📡 REST API

## Health Check

```http
GET /
```

Response

```json
{
  "message":"RAG PDF QA API Running 🚀"
}
```

---

## Upload PDF

```http
POST /upload
```

Response

```json
{
  "message":"PDF uploaded successfully.",
  "filename":"resume.pdf",
  "chunks":42
}
```

---

## Ask Question

```http
POST /ask
```

Request

```json
{
    "question":"What are the technical skills?"
}
```

Response

```json
{
  "question":"What are the technical skills?",
  "response":{
      "answer":"Python, FastAPI, LangChain, Machine Learning...",
      "sources":[
          {
            "file":"resume.pdf",
            "page":1
          }
      ]
  }
}
```

---

# 🔄 Workflow

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
Ask Question
      │
      ▼
Similarity Search
      │
      ▼
Retrieve Context
      │
      ▼
Generate Answer
      │
      ▼
Return Answer + Citations
```

---

# 🌟 Key Highlights

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search

✅ LangChain Integration

✅ Hugging Face LLM

✅ FAISS Vector Database

✅ FastAPI Backend

✅ Streamlit Frontend

✅ Dockerized Deployment

✅ Source Grounding

✅ Multi-PDF Support

---

# 🚀 Future Improvements

- 💬 Chat Memory
- 🌐 User Authentication
- 🔍 Hybrid Search (BM25 + Vector Search)
- 📁 DOCX, TXT & CSV Support
- ⚡ Streaming Responses
- 📊 Reranking Models
- ☁️ Cloud Deployment
- 🤖 Multi-LLM Support

---

# 📸 Demo

| Feature | Screenshot |
|----------|------------|
| Streamlit UI | Add Screenshot |
| Upload PDF | Add Screenshot |
| Ask Questions | Add Screenshot |
| Generated Answers | Add Screenshot |

---

# 👨‍💻 Author

**Your Name**

AI Engineer • Machine Learning • Generative AI • LangChain • FastAPI • Python

### Connect with me

- 💼 LinkedIn: https://linkedin.com/in/yourprofile
- 💻 GitHub: https://github.com/yourusername
- 📧 Email: your@email.com

---

# ⭐ Support

If you found this project helpful,

🌟 **Star this repository**

🍴 **Fork it**

🤝 **Contribute**

---

<p align="center">

### ⭐ Built with Python, LangChain, Hugging Face & FastAPI ⭐

**Happy Coding 🚀**

</p>

import os

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from app.config import (
    EMBEDDING_MODEL,
    LLM_MODEL,
    TOP_K
)

load_dotenv()

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# Load Local LLM
llm_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=os.environ["HF_TOKEN"],
    temperature=0.2,
    max_new_tokens=512
)

llm = ChatHuggingFace(
    llm=llm_endpoint
)


# Prompt Template
prompt = PromptTemplate(
    template="""
You are an AI assistant.

Answer ONLY from the given context.
If the answer is not present in the context, reply:
"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)


def ask_question(question: str):

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K}
    )

    # Retrieve relevant chunks
    docs = retriever.invoke(question)

    # Combine retrieved chunks
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Generate answer
    response = llm.invoke(
        prompt.format(
            context=context,
            question=question
        )
    )
    response = response.content

    # Collect source information
    sources = []

    for doc in docs:
        sources.append({
            "file": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", 0) + 1,
            "content": doc.page_content[:200]
        })

    # Return answer + sources
    return {
        "answer": response,
        "sources": sources
    }
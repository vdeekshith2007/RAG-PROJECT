from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load existing FAISS database
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


# User question
query = "What are the technical skills?"


# Search similar chunks
results = vectorstore.similarity_search(
    query,
    k=3
)


print("\nTop Relevant Chunks:\n")


for i, doc in enumerate(results):
    print("----------------------")
    print(f"Result {i+1}")
    print("----------------------")
    print(doc.page_content)
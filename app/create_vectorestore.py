from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


PDF_PATH = "data/sample.pdf"


# 1. Load PDF
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()


# 2. Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")


# 3. Create embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# 4. Create FAISS vector database
vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)


# 5. Save FAISS index
vectorstore.save_local("vectorstore")


print("FAISS vector database created successfully 🚀")
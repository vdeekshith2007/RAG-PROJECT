"""
Application Configuration
All configurable values should be kept here.
"""

# Embedding Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Local LLM
LLM_MODEL = "llama3.1"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 3

# Directories
UPLOAD_FOLDER = "uploads"
VECTORSTORE_FOLDER = "vectorstore"

# Allowed Files
ALLOWED_EXTENSION = ".pdf"
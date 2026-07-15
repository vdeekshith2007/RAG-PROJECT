from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


PDF_PATH = "data/sample.pdf"


# Load PDF
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

print(f"Total Pages: {len(documents)}")


# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


# Split documents into chunks
chunks = text_splitter.split_documents(documents)


print(f"Total Chunks Created: {len(chunks)}")


# Display sample chunks
for i, chunk in enumerate(chunks[:3]):
    print("\n----------------")
    print(f"Chunk {i+1}")
    print("----------------")
    print(chunk.page_content)
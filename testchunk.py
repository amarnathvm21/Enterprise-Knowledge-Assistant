from loaders import load_documents
from chunkers import split_docs

docs = load_documents(
    "data/handbook.pdf"
)

chunks = split_docs(
    docs
)

print("Chunks:", len(chunks))

print("\nFirst Chunk:\n")

print(
    chunks[0].page_content
)

print("\n",len(chunks))
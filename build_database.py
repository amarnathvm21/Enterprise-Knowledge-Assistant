from loaders import load_documents
from chunkers import split_docs
from embeddings import create_embeddings
from vector_store import create_vector_store

docs = load_documents(
    "data/handbook.pdf"
)

chunks = split_docs(
    docs
)

embed = create_embeddings()

db = create_vector_store(
    chunks,
    embed
)
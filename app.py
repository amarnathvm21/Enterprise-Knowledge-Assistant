from loaders import load_documents
from chunkers import split_docs
from embeddings import create_embeddings
from vector_store import create_vector_store
from retriever import search
from llm import ask_llm

docs = load_documents(
"data/handbook.pdf"
)

chunks = split_docs(
docs
)

embed = create_embeddings()

create_vector_store(
chunks,
embed
)

question = input(
"Ask:"
)

results = search(
question
)

context = "\n".join(
[
r.page_content
for r in results
]
)

answer = ask_llm(
context,
question
)

print("\nAnswer:")
print(answer)
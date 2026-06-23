from loaders import load_documents
from chunkers import split_docs
from embeddings import create_embeddings
from vector_store import create_vector_store

import os


all_docs = []

data_folder = "data"

for file in os.listdir(data_folder):

    if file.endswith(".pdf"):

        path = os.path.join(
            data_folder,
            file
        )

        docs = load_documents(
            path
        )

        all_docs.extend(
            docs
        )


print(
    "Documents loaded:",
    len(all_docs)
)


chunks = split_docs(
    all_docs
)

print(
    "Chunks:",
    len(chunks)
)


embeddings = create_embeddings()

create_vector_store(
    chunks,
    embeddings
)

print(
    "Index rebuilt successfully"
)
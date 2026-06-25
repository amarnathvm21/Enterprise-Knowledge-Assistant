import os

from loaders import load_documents
from chunkers import split_docs
from embeddings import create_embeddings
from vector_store import create_vector_store


def rebuild_index():

    all_docs = []

    for file in os.listdir("data"):

        if file.endswith(".pdf"):

            path = os.path.join(
                "data",
                file
            )

            docs = load_documents(path)

            all_docs.extend(docs)

    chunks = split_docs(
        all_docs
    )

    embeddings = create_embeddings()

    create_vector_store(
        chunks,
        embeddings
    )
    print(
        "Loaded documents:",
        len(all_docs)
    )
    return len(chunks)


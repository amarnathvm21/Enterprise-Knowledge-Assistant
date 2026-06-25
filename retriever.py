from langchain_community.vectorstores import FAISS
from embeddings import create_embeddings


embeddings = create_embeddings()


def load_db():

    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )


def search(question):

    db = load_db()

    results = db.similarity_search(
        question,
        k=3
    )

    return results
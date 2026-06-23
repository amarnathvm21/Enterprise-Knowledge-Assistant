from langchain_community.vectorstores import FAISS
from embeddings import create_embeddings


print("Loading embeddings...")

embeddings = create_embeddings()

print("Loading FAISS...")

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)


def search(question):

    results = db.similarity_search(
        question,
        k=1
    )

    return results
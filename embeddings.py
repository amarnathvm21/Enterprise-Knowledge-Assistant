# embedding.py

from langchain_community.embeddings import HuggingFaceEmbeddings


def create_embeddings():

    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return model

embed = create_embeddings()

vector = embed.embed_query(
    "What is leave policy?"
)

print(len(vector))
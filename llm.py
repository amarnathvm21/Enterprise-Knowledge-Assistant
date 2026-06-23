from langchain_ollama import ChatOllama


def ask_llm(context, question):

    llm = ChatOllama(
        model="phi3:mini"
    )

    prompt = f"""
Answer only from the context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content
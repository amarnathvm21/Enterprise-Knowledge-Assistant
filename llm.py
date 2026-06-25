from langchain_ollama import ChatOllama


def ask_llm(
    context,
    question,
    history
):

    llm = ChatOllama(
        model="phi3:mini"
    )

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Use the conversation history to understand follow-up questions.

Answer ONLY using the provided document context.

If the answer is not present in the context, say:

"I could not find that information in the uploaded documents."

Conversation History:
{history}

Document Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(
        prompt
    )

    return response.content
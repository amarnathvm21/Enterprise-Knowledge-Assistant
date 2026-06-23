from retriever import search
from llm import ask_llm

print("Starting...")

question = input("Ask: ")

print("Searching...")

results = search(question)

print("Retrieved")

context = "\n".join(
    [r.page_content for r in results]
)

print("Calling LLM...")

answer = ask_llm(
    context,
    question
)

print("LLM finished")

print("\nANSWER:\n")

print(answer)
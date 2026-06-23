import streamlit as st

from retriever import search
from llm import ask_llm


st.title(
    "Enterprise Knowledge Assistant"
)


question = st.text_input(
    "Ask Question"
)


if question:

    with st.spinner(
        "Thinking..."
    ):

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

        st.write(
            answer
        )
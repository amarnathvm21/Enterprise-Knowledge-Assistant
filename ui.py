import os
import shutil
import streamlit as st

from retriever import search
from llm import ask_llm
from build_index import rebuild_index


st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Enterprise Knowledge Assistant")


# =====================================
# Chat Memory
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =====================================
# PDF Upload Section
# =====================================

st.sidebar.header("Document Management")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs(
        "data",
        exist_ok=True
    )

    for file in uploaded_files:

        save_path = os.path.join(
            "data",
            file.name
        )

        with open(
            save_path,
            "wb"
        ) as f:

            f.write(
                file.getbuffer()
            )

    with st.spinner(
        "Building vector index..."
    ):

        chunk_count = rebuild_index()

    st.sidebar.success(
        f"Index rebuilt successfully ({chunk_count} chunks)"
    )


# =====================================
# Display Chat History
# =====================================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )


# =====================================
# Chat Input
# =====================================

question = st.chat_input(
    "Ask a question about your documents..."
)


if question:

    # Show user message

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # =====================================
    # Build Conversation History
    # =====================================

    history = ""

    for msg in st.session_state.messages[-6:]:

        history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    # =====================================
    # Retrieve Documents
    # =====================================

    with st.spinner(
        "Searching documents..."
    ):

        results = search(
            question
        )

    context = "\n".join(
        [
            doc.page_content
            for doc in results
        ]
    )


    # =====================================
    # Extract Citations
    # =====================================

    sources = []

    for doc in results:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            0
        )

        filename = os.path.basename(
            source
        )

        sources.append(
            f"{filename} (Page {page + 1})"
        )
    print(
        doc.metadata
    )

    # =====================================
    # Generate Answer
    # =====================================

    with st.spinner(
        "Generating answer..."
    ):

        answer = ask_llm(
            context,
            question,
            history
        )

    # =====================================
    # Save Assistant Response
    # =====================================

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # =====================================
    # Display Assistant Response
    # =====================================

    with st.chat_message(
        "assistant"
    ):

        st.markdown(answer)

        if sources:

            st.markdown("### Sources")

            for source in sorted(
                set(sources)
            ):

                st.markdown(
                    f"- {source}"
                )


if st.sidebar.button(
    "Clear Knowledge Base"
):

    shutil.rmtree(
        "faiss_index",
        ignore_errors=True
    )

    for file in os.listdir(
        "data"
    ):

        if file.endswith(".pdf"):

            os.remove(
                os.path.join(
                    "data",
                    file
                )
            )

    st.sidebar.success(
        "Knowledge base cleared"
    )
# Enterprise Knowledge Assistant (RAG-Based Document Q&A)

An AI-powered Enterprise Knowledge Assistant that allows users to ask natural language questions and receive answers directly from uploaded PDF documents.

This project uses a Retrieval-Augmented Generation (RAG) architecture to retrieve relevant information from enterprise documents and generate grounded responses using a local Large Language Model (LLM).

Built with LangChain, FAISS, Ollama, and Streamlit.

---

## Project Overview

Traditional chatbots generate responses without access to company-specific knowledge.

This application solves that problem by:

- Reading PDF documents
- Splitting them into searchable chunks
- Converting text into vector embeddings
- Storing embeddings in FAISS
- Retrieving relevant context
- Generating responses using a local LLM

Users can ask questions such as:

> "What is the leave policy?"

> "What are the office working hours?"

> "Summarize onboarding requirements."

---

## Features

- PDF document ingestion
- Automatic document chunking
- Vector similarity search using FAISS
- Retrieval-Augmented Generation (RAG)
- Local LLM inference using Ollama
- Interactive Streamlit web interface
- Modular and extensible architecture

---

## Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| LLM | Ollama |
| UI | Streamlit |

---

## Project Architecture

```text
PDF Documents
     ↓
Document Loader
     ↓
Text Chunking
     ↓
Embeddings
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Ollama LLM
     ↓
Final Response
```

---

## Folder Structure

```text
enterprise_knowledge_assistant/

│
├── data/
│   └── employee_handbook.pdf
│
├── faiss_index/
│
├── loaders.py
├── chunkers.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── llm.py
├── build_index.py
├── ui.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone <repository-url>
cd enterprise_knowledge_assistant
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama.

Official website:

https://ollama.com

Pull model:

```bash
ollama pull phi3:mini
```

Verify:

```bash
ollama run phi3:mini
```

---

## Add Documents

Place PDF files inside:

```text
data/
```

Example:

```text
data/
├── employee_handbook.pdf
├── onboarding_guide.pdf
```

---

## Build Vector Index

Run:

```bash
python build_index.py
```

This will:

- Load PDFs
- Split text
- Generate embeddings
- Build FAISS index

---

## Launch Application

Start Streamlit:

```bash
streamlit run ui.py
```

Open:

```text
http://localhost:8501
```

---

## Example Questions

```text
How many annual leaves are allowed?

What are office working hours?

Summarize onboarding instructions.
```

---

## Future Improvements

- Multi-document collections
- Metadata filtering
- Conversational memory
- User authentication
- Cloud deployment
- Incremental indexing
- Docker support

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- Semantic search
- Local LLM deployment
- Document processing pipelines
- AI application development

---

## Author

Developed as a portfolio project to demonstrate practical AI engineering and document intelligence workflows.

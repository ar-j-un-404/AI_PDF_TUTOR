# AI PDF Tutor

An AI-powered PDF question-answering application built with Python, Streamlit, Ollama, Llama 3.2, and Sentence Transformers.

**AI PDF Tutor is a Retrieval-Augmented Generation (RAG) system that combines semantic search with a local Large Language Model to generate context-aware answers from PDF documents.**

---

## About the Project

AI PDF Tutor is a Retrieval-Augmented Generation (RAG) application that retrieves relevant information from a PDF using embeddings and cosine similarity, then uses a local LLM (Llama 3.2) to generate answers based only on the retrieved context.

Unlike traditional chatbots, the model does not rely solely on its internal knowledge. Instead, it performs semantic search on the PDF contents and produces document-grounded responses.

---

## Features

* PDF text extraction using PyPDF
* Semantic search using Sentence Transformers
* Embedding-based document retrieval
* Cosine similarity ranking
* Top-K context retrieval
* Local AI inference using Ollama
* Llama 3.2 integration
* Context-aware question answering
* Session-based conversation memory
* Streamlit web interface
* Modular architecture
* Offline execution after model download
* Replaceable PDF documents
* Demo PDF included (`work_pdf.pdf`)
* Retrieval-Augmented Generation (RAG) architecture

---

## Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3.2
* Sentence Transformers
* NumPy
* PyPDF

---

## Architecture

```text
PDF
↓
Text Extraction
↓
Chunk Creation
↓
Embedding Generation
↓
Semantic Search
↓
Cosine Similarity
↓
Top-K Retrieval
↓
Llama 3.2 (Ollama)
↓
Answer Generation
↓
Streamlit Interface
```

---

## Project Structure

```text
AI_PDF_TUTOR
│
├── .gitignore
├── README.md
├── requirements.txt
├── ai_engine.py
├── app.py
└── work_pdf.pdf
```

---

## Demo PDF

A sample file named `work_pdf.pdf` is included in this repository for demonstration purposes.

You can test the application immediately using this file or replace it with your own PDF to ask questions about different documents.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ar-j-un-404/AI_PDF_TUTOR.git
```

Move into the project directory:

```bash
cd AI_PDF_TUTOR
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open your browser and go to:

```text
http://localhost:8501
```

---

## Current Capabilities

* Single PDF support
* Semantic document retrieval
* Session-based conversation memory
* Local LLM inference
* Context-aware responses
* Fully local execution

---

## Future Improvements

Planned enhancements include:

* Support for multiple PDF documents
* PDF upload through the Streamlit interface
* Persistent memory across sessions
* Chat history storage
* Better chunking strategies
* Citation and page number references
* FAISS or ChromaDB vector database integration
* OCR support for scanned PDFs
* Support for larger language models
* Voice input and text-to-speech output
* Cloud deployment
* User authentication and document management
* Streaming responses
* Source highlighting

---

## Author

**Arjun**

---

## License

This project is intended for educational and learning purposes.

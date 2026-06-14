# AI PDF Tutor

An AI-powered PDF question-answering application built with Python, Streamlit, Ollama, and Sentence Transformers.

## Features

- Ask questions about a PDF
- Semantic search using embeddings
- Local LLM with Ollama and Llama 3.2
- Streamlit web interface
- Context-aware answers based on PDF content

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Sentence Transformers
- NumPy
- PyPDF

## Project Structure

```
AI_PDF_TUTOR
│
├── app.py
├── ai_engine.py
├── work_pdf.pdf
├── README.md
└── .gitignore
```

## How to Run

Install dependencies:

```bash
pip install streamlit pypdf ollama sentence-transformers numpy
```

Start the application:

```bash
streamlit run app.py
```

## Author

Arjun
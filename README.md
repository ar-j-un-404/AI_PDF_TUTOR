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

## Demo PDF

A sample file named `work_pdf.pdf` is included in this repository for demonstration purposes. You can replace it with your own PDF to ask questions about different documents.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## Project Structure

```
AI_PDF_TUTOR
│
├── .gitignore
├── README.md
├── requirements.txt
├── ai_engine.py
├── app.py
└── work_pdf.pdf
```

## Author

Arjun
from pypdf import PdfReader
from ollama import chat
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

reader = PdfReader("work_pdf.pdf")

chunks = []

for page in reader.pages:

    text = page.extract_text()

    if text:

        chunks.append(text)

chunk_embeddings = model.encode(chunks)

messages = []


def get_answer(question):

    question_embedding = model.encode(question)

    scores = []

    for embedding in chunk_embeddings:

        score = np.dot(question_embedding, embedding) / (
            np.linalg.norm(question_embedding)
            * np.linalg.norm(embedding)
        )

        scores.append(score)

    top_indices = np.argsort(scores)[-5:]

    context = ""

    for index in top_indices:

        context = context + chunks[index] + "\n"

    messages.append(
        {
            "role": "user",
            "content": f"""
You are an AI PDF tutor.

Answer ONLY using the information provided in the context below.

If the answer is not present in the context, say:

I could not find that information in the PDF.

Context:
{context}

Question:
{question}
"""
        }
    )

    response = chat(
        model="llama3.2:3b",
        messages=messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content
        }
    )

    return response.message.content
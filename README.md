This is my AI project, built as a learning experience from scratch. The goal of this project is simple:

> Upload a PDF → Ask questions → Get accurate answers from the document

This project is designed and documented **for beginners**, especially for someone who is **not an AI engineer** and is learning concepts like embeddings, chunking, retrieval, tokens, and context windows for the first time.


## What This Project Does

- Users upload a **PDF document**
- The system **reads and splits (chunks)** the document
- Relevant parts of the document are **retrieved** based on the question
- An AI model generates an **answer grounded in the document content**

This is commonly called a **Document Q&A system** or **RAG (Retrieval-Augmented Generation)** system.

## 🧠 Why I Built This Project

I built this project to:

- Understand **how AI reads long documents**
- Learn why **LLMs cannot read entire PDFs at once**
- Learn about:
  - Chunking
  - Embeddings
  - Similarity search
  - Context window limits
  - Tokens (the hard way 😅)
- Create something **resume-worthy** and **GitHub-ready**

This project helped me move from *“AI feels like magic”* to *“Oh, this is how it actually works.”*


## Core Concepts (Explained Simply)

### Why We Can’t Just Upload a PDF to AI

Large Language Models (LLMs) have a **context window**.

That means:
- They can only read a **limited number of tokens at once**
- Large PDFs exceed this limit

 **Tokens ≠ words**
- 1 word ≈ 1–3 tokens
- A 30-page PDF can easily be **20,000+ tokens**

So instead of sending the entire document, we must **split it into pieces**.

### Chunking the Document

**Chunking** means splitting the document into small, manageable text pieces.

Example:
- Each chunk = 300–500 words
- Small overlap between chunks (to avoid missing context)

Why chunking is important:
- Fits into the model’s context window
- Improves retrieval accuracy
- Reduces hallucinations

### Embeddings (How AI Understands Meaning)

Each chunk is converted into a **vector embedding**.

Think of embeddings like:
> A numeric fingerprint of the meaning of text

This allows us to:
- Compare a user question with document chunks
- Find the **most relevant sections** using similarity search

### Retrieval (Finding the Right Chunks)

When a user asks a question:

1. The question is converted into an embedding
2. We compare it with all chunk embeddings
3. We retrieve the **top K most relevant chunks**

Only these chunks are sent to the LLM.

This is the **most important step** for accuracy.

### Answer Generation

The retrieved chunks are passed to the language model along with:

- The user question
- Clear instructions like:

> "Answer only using the provided context. If the answer is not in the document, say you don’t know."

This reduces hallucinations and keeps answers grounded.

## Project Architecture

text
User
  ↓
Upload PDF
  ↓
PDF Text Extraction
  ↓
Chunking
  ↓
Embeddings Creation
  ↓
Vector Store
  ↓
User Question
  ↓
Similarity Search
  ↓
Relevant Chunks
  ↓
LLM Answer

## Tech Stack (Beginner-Friendly)

* **Python**
* **PDF parsing** (PyPDF / pdfplumber)
* **Embeddings** (OpenAI / Sentence Transformers)
* **Vector store** (FAISS / Chroma)
* **LLM** (OpenAI / local model)
* **Streamlit or CLI** for UI

##  Project Structure

```bash
document-qa-system/
│── data/
│   └── sample.pdf
│── ingest.py        # PDF loading + chunking
│── embeddings.py    # Create and store embeddings
│── query.py         # Ask questions
│── utils.py
│── app.py           # UI (optional)
│── requirements.txt
│── README.md
```

## What I Learned (Honest Takeaways)

* AI is **not magic** — it’s careful engineering
* Chunk size matters a lot
* More context ≠ better answers
* Retrieval quality > model size
* Token limits will break your app if ignored

I also learned how to **debug bad answers** by checking:

* Wrong chunk retrieval
* Too much or too little context
* Poor chunk overlap

## How This Project Can Be Improved

Future improvements:

* Support for multiple PDFs
* Citation-based answers
* Highlighting source text
* Chat history memory
* Upload limits & error handling

## 🎯 Who This Project Is For

* Beginners in AI / ML
* Software engineers new to LLMs
* Students building their **first AI portfolio project**

If you can build this, you understand **real-world LLM applications**.

## Final Thoughts

This project taught me how **modern AI applications actually work** behind the scenes.

If you’re new to AI:

> **Build this before anything else.**

It will change how you think about LLMs forever.

*This repository is intentionally beginner-friendly and heavily documented so others can learn the same way I did.*

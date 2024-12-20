

# RAG Model with Generative AI for Querying Markdown Files

This project implements **Retrieval-Augmented Generation (RAG)** to query any `.md` (Markdown) file by embedding its content into a vector database and performing semantic searches. 

## Features
- **Chunking and Embedding**: The content of the `.md` file is chunked into smaller, meaningful sections using the **Markdown Text Splitter**. These chunks are then embedded using the **HuggingFaceEmbeddings** model from **Langchain** and stored in a **Chroma Vector Database**.
- **RAG Approach**: When a user submits a query, the application retrieves relevant chunks from the vector database and feeds them into the **Meta-Llama-3.1-8B-Instruct-Turbo** model via **Throught.ai** to generate a context-based grounded response.

## Tools Used
- **Hugging Face**: For text embeddings
- **Chroma DB**: For storing vector embeddings
- **Langchain**: For managing embeddings, prompt templates, and LLM interaction
- **Streamlit**: For the application interface
- **Markdown Text Splitter**: For chunking the `.md` file

This RAG-based setup allows the application to answer questions based on the content of any `.md` file, providing accurate, context-driven responses.

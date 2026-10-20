# DocuRAG — AI-Powered PDF Question Answering

An LLM-powered **Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask questions in natural language. DocuRAG retrieves relevant document content and uses Google Gemini to generate concise, context-aware answers.

**[Live Demo](https://docurag-lcgeovabypejzwz383dj3k.streamlit.app/) · [GitHub Repository](https://github.com/impulsiveblast/DocuRAG)**

## Features

- **PDF Ingestion:** Upload PDF documents through an interactive interface.
- **Text Chunking:** Split extracted document text into manageable chunks using `RecursiveCharacterTextSplitter`, with a chunk size of 1,000 characters and an overlap of 200 characters.
- **Semantic Embeddings:** Generate document embeddings using Google's Gemini embedding model.
- **Vector-Based Retrieval:** Retrieve the two most relevant document chunks for a user query using `InMemoryVectorStore`.
- **LLM-Powered Answers:** Use Google Gemini to generate concise responses grounded in retrieved document context.
- **Conversational Interface:** Interact with uploaded documents through Streamlit's chat interface.
- **Cloud Deployment:** Access the application through Streamlit Community Cloud.

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| LLM | Google Gemini |
| Embeddings | Google Gemini Embeddings |
| RAG Framework | LangChain |
| PDF Processing | PyPDFLoader, PyPDF |
| Text Splitting | RecursiveCharacterTextSplitter |
| Vector Store | InMemoryVectorStore |
| User Interface | Streamlit |
| Deployment | Streamlit Community Cloud |

## How It Works

1. **Upload:** The user uploads a PDF document.
2. **Extract:** `PyPDFLoader` extracts the document's text and page metadata.
3. **Chunk:** The extracted text is split into overlapping chunks.
4. **Embed:** Google Gemini Embeddings converts the chunks into vector representations.
5. **Store:** The embeddings and document chunks are stored in an in-memory vector store.
6. **Retrieve:** The user's question is used to retrieve the top two semantically relevant chunks.
7. **Generate:** Google Gemini receives the retrieved context and question to generate an answer.
8. **Display:** The answer appears in the Streamlit chat interface.

## Getting Started

### Prerequisites

- Python 3.10 or newer
- A Google Gemini API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/impulsiveblast/DocuRAG.git
cd DocuRAG
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.streamlit/secrets.toml` file in the project directory:

```toml
GOOGLE_API_KEY = "your_google_gemini_api_key"
```

Obtain your API key through [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your API key, `.env` file, or `secrets.toml` file to GitHub. Keep credentials in local secrets and configure the same `GOOGLE_API_KEY` secret in Streamlit Community Cloud for deployment.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, upload a PDF, and start asking questions.

## Testing

Tested the RAG chatbot on **25+ PDF documents**, delivering accurate, context-grounded answers to questions based on retrieved document content.

## Limitations

- The vector store is in-memory; document embeddings are not persisted across application restarts.
- Retrieval is limited to the two most relevant chunks per query.
- Answer quality depends on the PDF's text extraction quality, retrieval relevance, and the LLM's response.
- The application is designed for document question answering and is not a substitute for professional medical or other expert advice.

## Future Improvements

- Persistent vector storage for reusable document embeddings.
- Support for multiple documents within a single knowledge base.
- Source citations and page-level references in generated answers.
- Retrieval evaluation, answer-quality metrics, and hallucination checks.
- A FastAPI backend to support integration with custom frontend applications.

## Author

**Brahamjeet Anand**

- GitHub: [@impulsiveblast](https://github.com/impulsiveblast)

---

*Built to explore practical applications of Retrieval-Augmented Generation, semantic search, and large language models.*

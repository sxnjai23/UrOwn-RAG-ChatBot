# Q&A Chatbot - RAG Application

A powerful **Retrieval-Augmented Generation (RAG)** chatbot application built with LangChain, LangGraph, and Streamlit. Ask questions about your documents and get intelligent, context-aware answers powered by the Llama 3.1 LLM via Groq API.

## 🎯 Features

- **Document Processing**: Automatically ingest and process PDF documents
- **Vector Database**: Uses Chroma for fast semantic search across documents
- **Smart Embeddings**: HuggingFace embeddings (all-MiniLM-L6-v2) for document understanding
- **Advanced LLM**: Powered by Llama 3.1 (8B) via Groq API for fast inference
- **Interactive UI**: Clean, intuitive Streamlit interface for asking questions
- **Conversation Memory**: Maintains conversation history using LangGraph checkpointing
- **Production-Ready**: Modular architecture with configuration management

## 📋 Tech Stack

- **Python**: 3.12+
- **Frontend**: Streamlit 1.58.0+
- **LLM Orchestration**: LangChain 1.3.4+, LangGraph 1.2.4+
- **Vector Database**: ChromaDB 1.5.9+
- **Embeddings**: Sentence Transformers / HuggingFace 5.5.1+
- **LLM Provider**: Groq API (Llama 3.1 8B)
- **Document Processing**: PyPDF 6.13.1+
- **Data Processing**: Pandas 3.0.3+

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip or uv package manager
- Groq API key

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Q&A_Chatbot
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

Using pip:
```bash
pip install -e .
```

Or using uv (faster):
```bash
uv sync
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your Groq API key from [Groq Console](https://console.groq.com/).

### Step 5: Prepare Documents

Place your PDF documents in the `data/` directory:

```bash
mkdir data
# Copy your PDF files to the data/ directory
```

## 📖 Usage

### Step 1: Ingest Documents

Run the ingestion script to process PDFs and create the vector database:

```bash
python ingest.py
```

This will:
- Load all PDFs from the `data/` directory
- Split documents into chunks (500 tokens, 50 token overlap)
- Generate embeddings using HuggingFace
- Store vectors in ChromaDB (`docs/chroma/`)

### Step 2: Start the Chatbot

Launch the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Step 3: Ask Questions

1. Upload PDF documents using the file uploader (optional - uses pre-ingested documents)
2. Type your question in the chat interface
3. Get instant answers based on your documents

## 📁 Project Structure

```
Q&A_Chatbot/
├── app.py                          # Streamlit UI & LangGraph workflow
├── ingest.py                       # Document ingestion pipeline
├── config.py                       # Configuration management
├── main.py                         # Entry point
├── pyproject.toml                  # Project metadata & dependencies
├── README.md                       # This file
├── .env                           # Environment variables (create this)
├── data/                          # PDF documents to ingest
│   └── (your PDF files here)
└── docs/
    └── chroma/                    # Vector database persistence
        ├── chroma.sqlite3
        └── (embedding data)
```

## 🔧 Configuration

Edit `config.py` to customize:

| Setting | Default | Description |
|---------|---------|-------------|
| `PDF_SOURCE_DIRECTORY` | `data` | Directory containing PDF documents |
| `CHROMA_PERSIST_DIRECTORY` | `docs/chroma` | Vector database storage location |
| `EMBEDDING_MODEL_NAME` | `all-MiniLM-L6-v2` | HuggingFace embedding model |
| `CHUNK_SIZE` | `500` | Document chunk size (tokens) |
| `CHUNK_OVERLAP` | `50` | Overlap between chunks (tokens) |

## 🎮 Usage Examples

### Upload and Chat

1. Open the Streamlit app
2. Use the file uploader to add new PDFs (optional)
3. Ask questions like:
   - "What is the main topic of this document?"
   - "Summarize the key points about [topic]"
   - "What does the document say about [specific term]?"

### Command Line Ingestion

```bash
python ingest.py
```

## 🔐 API Keys & Security

- Keep your `GROQ_API_KEY` secret - never commit `.env` to version control
- The `.env` file is excluded via `.gitignore`
- Use environment variables for all sensitive data

## 🏗️ Architecture

```
User Input (Streamlit UI)
    ↓
LangGraph Workflow
    ├─ SystemPrompt + Context
    ├─ Chroma Vector Search
    └─ Groq LLM Inference
    ↓
Response Display
```

## 📊 How RAG Works

1. **Retrieval**: User question is embedded and semantically similar document chunks are retrieved from Chroma
2. **Augmentation**: Retrieved context is combined with the user's question
3. **Generation**: The Groq LLM generates an answer based on the augmented prompt
4. **Memory**: Conversation history is maintained via LangGraph checkpointing

## 🐛 Troubleshooting

### ChromaDB Not Found
- Ensure you've run `python ingest.py` to create the vector database
- Check that `docs/chroma/` directory exists and contains data

### Missing Groq API Key
- Create a `.env` file with `GROQ_API_KEY=your_key_here`
- Get your key from [Groq Console](https://console.groq.com/)

### PDF Loading Errors
- Ensure PDFs are valid and not corrupted
- Place PDFs in the `data/` directory
- Check file permissions

### Embedding Model Download
- First run will download the embedding model (~90MB)
- Requires internet connection
- Subsequent runs use cached model

## 📝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📄 License

This project is provided as-is for educational and development purposes.

## 🤝 Support

For issues, questions, or suggestions, please open an issue on the repository.

---

**Last Updated**: 2026-06-09  
**Project Name**: Ur-own RAG Bot 
**Version**: 0.1.0


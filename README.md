# DocQ-Llama-3.3-70B-Versatile
# 🦙❓ DocQ Chat – Talk. Ask. Know.

## 📖 Introduction

DocQ Chat is an AI-powered document query system that allows users to upload PDF files and ask questions about their contents. It leverages state-of-the-art natural language processing (NLP) and retrieval-augmented generation (RAG) techniques to provide contextual and meaningful responses. 

## 🔍 How It Works

1. **Upload a PDF File** – The user uploads a document via the Streamlit interface.
2. **Process the Document** – The document is processed using an advanced text splitter to break it into smaller, manageable chunks.
3. **Store in Vector Database** – The extracted text chunks are stored in a FAISS vector database using Hugging Face embeddings.
4. **Query & Retrieval** – The user asks a question, which is processed using the Llama-3 model via Groq API.
5. **Contextual Chat** – The system maintains conversation memory, allowing contextual responses over multiple exchanges.
6. **Get Answers** – The AI retrieves relevant text chunks and generates precise answers.

## 🏗️ Tech Stack

The project utilizes the following technologies:

- **Python** – Core programming language
- **Streamlit** – Web-based UI framework
- **FAISS** – Vector database for efficient search
- **Hugging Face Transformers** – Used for embeddings
- **LangChain** – Manages LLM-based retrieval and conversations
- **Groq API** – Provides fast LLM inference
- **Unstructured.io** – Handles document parsing
- **Dotenv** – Manages environment variables

## 📸 Screenshots

### 1️⃣ Uploading a PDF File
![Screenshot 2025-04-02 014126](https://github.com/user-attachments/assets/ec455734-da4f-4d22-bf68-21777b91fce2)

### 2️⃣ Asking a Question
![Screenshot 2025-04-02 014139](https://github.com/user-attachments/assets/0e9aab84-3f82-4ecb-bb44-c02a1abf74e0)

### 3️⃣ Context-Aware Responses
![Screenshot 2025-04-02 014150](https://github.com/user-attachments/assets/9c1c492b-8f76-45d8-aeca-fdaf33781ddc)

## ⚙️ Installation Guide

### 1️⃣ Create & Activate a Conda Environment

```bash
conda create --name venv python=3.10 -y
conda activate venv
```
### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
### 3️⃣ Setup Environment Variables

```bash
echo "GROQ_API_KEY=your_api_key_here" > src/.env
```
### 4️⃣ Run the Application

```bash
streamlit run src/main.py
```

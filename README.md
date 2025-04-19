# DocQ Chat :

## Introduction

DocQ Chat is an AI-powered document query system that allows users to upload PDF files and ask questions about their contents. It leverages state-of-the-art NLP and RAG techniques to provide contextual and meaningful responses. This version features a Flask backend and a separate frontend.

## How It Works

1.  **Upload a PDF File** – The user uploads a document via the web interface.
2.  **Backend Processes Document** – The Flask backend processes the uploaded PDF using an advanced text splitter to break it into smaller, manageable chunks.
3.  **Store in Vector Database** – The extracted text chunks are stored in a FAISS vector database using Hugging Face embeddings.
4.  **Query & Retrieval** – When the user asks a question via the frontend, it's sent to the Flask backend, which processes it using the Llama-3 model via Groq API.
5.  **Contextual Chat** – The backend maintains conversation memory, allowing contextual responses over multiple exchanges.
6.  **Backend Retrieves & Generates Answer** – The AI retrieves relevant text chunks and generates precise answers, sending them back to the frontend.
7.  **Frontend Displays Answer** – The web interface displays the AI's response to the user.

## Tech Stack

**Frontend:**

-   **HTML** – Structure of the web interface
-   **CSS** – Styling of the web interface
-   **JavaScript** – Interactivity and communication with the backend

**Backend:**

-   **Python** – Core programming language
-   **Flask** – Web framework for the backend API
-   **FAISS** – Vector database for efficient search
-   **Hugging Face Transformers** – Used for embeddings
-   **LangChain** – Manages LLM-based retrieval and conversations
-   **Groq API** – Provides fast LLM inference
-   **Unstructured.io** – Handles document parsing
-   **Dotenv** – Manages environment variables

##  Screenshots

### 1. Asking a Question 
![Screenshot 2025-04-19 165203](https://github.com/user-attachments/assets/175e196a-4930-48b7-a2cb-fdbd82482439)

### 2. Context-Aware Responses
![Screenshot 2025-04-19 165215](https://github.com/user-attachments/assets/c7b4ac5c-e7cf-45a0-8b8f-cd9f6dfc1650)

##  Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/akansh30/DocQ-Chat.git
cd DocQ-Chat
```
### 2. Setup Backend Environment
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   
```
### 3. Create a .env file and add API Key
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```
### 4. Install Backend Dependencies
```bash
Install Backend Dependencies
```
### 5. Run the Backend Application
```bash
cd backend
python app.py
```
### 6. Run the Frontend Application
```bash
cd ..
cd frontend
python -m http.server 5500
```
The frontend will be accessible in your web browser at http://localhost:5500


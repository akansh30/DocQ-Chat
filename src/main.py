import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()
working_dir = os.path.dirname(os.path.abspath(__file__))

# Function to load the document
def load_document(file_path):
    loader = UnstructuredPDFLoader(file_path)
    documents = loader.load()
    return documents

# Function to process and store documents
def setup_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings()
    
    #  Use RecursiveCharacterTextSplitter (handles large PDFs better)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=100
    )
    doc_chunks = text_splitter.split_documents(documents)

    # Store in FAISS vector database
    vectorstore = FAISS.from_documents(doc_chunks, embeddings)
    return vectorstore

# Function to create the retrieval chain
def create_chain(vectorstore):
    llm = ChatGroq(
        model="Llama-3.3-70B-Versatile",  
        temperature=0
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  
    
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )
    return chain

# Streamlit UI
st.set_page_config(
    page_title="Doc Q ",
    page_icon="❓",
    layout="centered"
)

st.title("🦙❓DocQ Chat – Talk. Ask. Know.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDF
uploaded_file = st.file_uploader(label="Upload your PDF file", type=["pdf"])

if uploaded_file:
    file_path = f"{working_dir}/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process only once to avoid repeated computation
    if "vectorstore" not in st.session_state:
        documents = load_document(file_path)
        st.session_state.vectorstore = setup_vectorstore(documents)

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = create_chain(st.session_state.vectorstore)

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
user_input = st.chat_input("Ask DocQ..")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = st.session_state.conversation_chain.invoke({"question": user_input})
        assistant_response = response["answer"]
        st.markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

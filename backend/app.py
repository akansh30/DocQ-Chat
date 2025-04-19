import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from rag_chain import get_chain, get_or_create_vectorstore
import uuid

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

conversation_chain = None

@app.route("/upload", methods=["POST"])
def upload_file():
    global conversation_chain

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    vectorstore = get_or_create_vectorstore(file_path)
    conversation_chain = get_chain(vectorstore)

    return jsonify({"message": "File uploaded and processed."}), 200

@app.route("/ask", methods=["POST"])
def ask_question():
    global conversation_chain
    if not conversation_chain:
        return jsonify({"error": "Upload a PDF first."}), 400

    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided."}), 400
    
    response = conversation_chain.invoke({"question": question})
    print("Response from chain:", response)

    answer = response.get("answer") or response.get("result") or str(response)
    return jsonify({"answer": answer})

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

if __name__ =="__main__":
    app.run(debug=True)

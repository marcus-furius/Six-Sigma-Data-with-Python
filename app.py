from flask import Flask, request, jsonify
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate

app = Flask(__name__)

# Load stored embeddings and vector store
persist_directory = "db"
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=OllamaEmbeddings(model="llama3.1"))

# Load the LLaMA 3.1 model
llm = Ollama(model="llama3.1")

# Create a retrieval-based QA chain
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever(), chain_type="stuff")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    response = qa_chain.run(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

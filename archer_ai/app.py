"""
Large Language Model Retreival Augmented Generation (LLM RAG)

- This LLM RAG is using ollama to run llama3 (Meta / Meta-llama-3-8Billion)
- This LLAMA3 is 1 day old and leading the charts.

"""

from flask import Flask, render_template, request
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
from waitress import serve
import os.path
import webbrowser

app = Flask(__name__, template_folder="templates")

documents = SimpleDirectoryReader("data").load_data()

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3.2", request_timeout=30.0)

# Index the documents (Not persistant. Stores in memory.)
#index = VectorStoreIndex.from_documents(
#    documents,
#)

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# Either way we can now query the index
    #query_engine = index.as_query_engine()
    #response = query_engine.query("When was your last update?")
    #print(response)

@app.route("/") 
def hello(): 
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')  # Retrieve from JS
    print(data)

    query_engine = index.as_query_engine()
    prompt = data
    response = query_engine.query(prompt)
    print(response)
    result = response
    
    return str(result)

webbrowser.open('http://127.0.0.1:51434')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=51434)
#app.run(host="127.0.0.1", port=54932)

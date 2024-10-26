from flask import Flask,render_template, request
import qdrant_client
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader, StorageContext
import webbrowser

app = Flask(__name__,template_folder="templates")
# Loading the documents from the disk
documents = SimpleDirectoryReader('data').load_data()
# Initializing the vector store with Qdrant
client = qdrant_client.QdrantClient(path="./qdrant_data")
vector_store = QdrantVectorStore(client=client, collection_name="reggie")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
# Initializing the Large Language Model (LLM) with Ollama
# The request_timeout may need to be adjusted depending on the system's performance capabilities
llm = Ollama(model="llama3.2")
service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")
# Creating the index, which includes embedding the documents into the vector store
index = VectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)

@app.route("/") 
def hello(): 
	return render_template('index.html') 

@app.route('/process', methods=['POST'])
def process():

	data = request.form.get('data')  # Retrieve from JS
	print(data)

	query_engine = index.as_query_engine()
	prompt = (data)
	response = query_engine.query(prompt)
	print(response)
	result = (response)
	#with open("data/data.txt", "a") as text_file: print("Question : ", data, file=text_file)
	#with open("data/data.txt", "a") as text_file: print("Answer : ", response, file=text_file)
	return str(result)

webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
	app.run()
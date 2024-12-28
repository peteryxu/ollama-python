import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import StorageContext, load_index_from_storage

# Set up Ollama
llm = Ollama(model="llama3.2")
Settings.llm = llm
embed_model = OllamaEmbedding(model_name="granite-embedding")
Settings.embed_model = embed_model

# Define the path to your document directory
directory_path = 'data'

# Load documents
documents = SimpleDirectoryReader(directory_path).load_data()

# Create index
index = VectorStoreIndex.from_documents(documents, show_progress=True)

# Create query engine
query_engine = index.as_query_engine(llm=llm)

# Perform a query
response = query_engine.query("What is LlamaIndex?")
print(response)


# Save the index
index.storage_context.persist("index")

# Load a previously saved index
storage_context = StorageContext.from_defaults(persist_dir="index")
loaded_index = load_index_from_storage(storage_context)
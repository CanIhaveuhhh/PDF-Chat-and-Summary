import os

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

os.environ["OPENAI_API_KEY"] = ""

# LOAD PDF FILES USING LANGCHAIN LOADER

# Create a directory loader with the path to the directory and the glob pattern to match files
textinputs = DirectoryLoader(path="")

# Load the documents from the directory
docs = textinputs.load()

# Print the number and titles of the documents
print(len(docs))
for doc in docs:
    print(doc)

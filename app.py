# Create virtual environment: python3 -m venv env
# Activate virtual environment: source env/bin/activate
# At the end: deactivate


import streamlit as st
import pandas as pd
import chardet
import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to SOPythonData.csv
csv_file_path = os.path.join(current_dir, 'Data', 'SOPythonData.csv')

# Detect the encoding of the CSV file
with open(csv_file_path, 'rb') as f:
    result = chardet.detect(f.read())

# Print the detected encoding
print(result['encoding'])

# Use the detected encoding to read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, encoding=result['encoding'])

# Print the first few rows of the DataFrame
st.write(df.head())


# import chardet

# with open('Data/SOPythonData.csv', 'rb') as f:
#     result = chardet.detect(f.read())

# print(result['encoding'])

# load_dotenv() # This loads the OPENAI API Key from .env

# # Step 1: Load and preprocess the CSV data
# csv_path = "Data/SOPythonData.csv"

# df = pd.read_csv(csv_path) # Read the CSV file into a DataFrame
# df_selected = df[['q_body', 'a_body']] # Select only the relevant columns

# # Convert the DataFrame to a list of dictionaries, each representing a document
# documents = df_selected.apply(lambda row: {'q_body': row['q_body'], 'a_body': row['a_body']}, axis=1).tolist()

# # Print the first document to verify
# print(documents[0])


# Step 2: Vectorize the Q&A CSV data

# loader = CSVLoader(file_path="/Data/SOPythonData.csv")
# documents = loader.load()

#  # print(documents[0])

# embeddings = OpenAIEmbeddings()
# db = FAISS.from_documents(documents, embeddings)

# Step 3: Create a function for similarity search

# Step 4: Setup LLMChain and prompts

# Step 5: Retrieval augmented generation
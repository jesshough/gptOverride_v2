# Create virtual environment: python3 -m venv env
# Activate virtual environment: source env/bin/activate
# At the end: source deactivate


# Streamlit: streamlit run app.py
# Control C to quit

import time
import streamlit as st
import pandas as pd
import chardet
import os
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore

# Load environment variables from .env file
load_dotenv()

# ----------------------------------------
# Step 1: Load and preprocess the CSV data
# ----------------------------------------

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to SOPythonData.csv
csv_file_path = os.path.join(current_dir, 'Data', 'SOPythonData.csv')
print(csv_file_path)

# My column names got cut out of the CSV file, so I'm manually specifying:
column_names = ['Id', 'q_Score', 'q_Title', 'q_Body', 'a_Score', 'a_Body', 't_Tag']  # Replace with actual column names

# Read the CSV file in chunks
chunk_size = 1000
num_chunks = 50   # Number of chunks to read and process

chunks = []
for i, chunk in enumerate(pd.read_csv(csv_file_path, encoding='MacRoman', names=column_names, header=0, chunksize=chunk_size)):
    chunks.append(chunk)
    if i + 1 >= num_chunks:
        break

df = pd.concat(chunks, ignore_index=True)

df_selected = df[['q_Body', 'a_Body']] # Select only the relevant columns

# Save the selected columns to a new CSV file for use with LangChain
selected_csv_file_path = os.path.join(current_dir, 'Data', 'SelectedSOPythonData.csv')
df_selected.to_csv(selected_csv_file_path, index=False)

# ----------------------------------
# Step 2: Vectorize the Q&A CSV data
# ----------------------------------

# Load the preprocessed CSV file using CSVLoader
loader = CSVLoader(file_path=selected_csv_file_path)
documents = loader.load()
#print(len(documents))

# Get the API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Validate that the API key is correctly loaded
if openai_api_key is None:
    raise ValueError("The OpenAI API key is not found. Make sure it is set in the .env file and make sure money is loaded.")

# Proceed with LangChain processing
embeddings = OpenAIEmbeddings(api_key=openai_api_key)
db = FAISS.from_documents(documents, embeddings)

# Example usage
print(documents[0])

# -----------------------------------------------
# Step 3: Create a function for similarity search
# -----------------------------------------------

def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3) # 3 results most similar to the query, don't make it
    # too big - be aware of the contenxt limit for LLM
    page_contents_array = [doc.page_content for doc in similar_response] # can't print similar_response directly
    # because it will also have metadata, titles, etc. that we don't need. So this extracts just the data that we need.
    print(page_contents_array)
    return page_contents_array

# # This is just an example. At this point in the code, it should just return whatever q&a pair it thinks
# # is most similar to my question query. We don't have the LLM yet, so it will return the exact data from
# # our file.
# question_query = """
# How can I get a preview of a pdf on my Windows computer? I want the preview to be a jpeg.

# """
# results = retrieve_info(question_query)
# print(results)

# ----------------------------------
# Step 4: Setup LLMChain and prompts
# ----------------------------------

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

# Note the difference between answer with and without rule 4 below!!
template = """
You are a technical assistant who gives Python advice and you respond to questions
asked in a Python forum. 
I will share a user's question with you and you will give me the best answer that should be used
to repond to the user's question(s), 
and you will follow ALL of the rules below:

1/ Even if a user doesn't specify which language they are asking about, you need to assume it is Python.
 
2/ If a user is working on a Python project but their question is about a non-python aspect of the project, 
then you need to make sure to give appropriate techincal advice, aka tips/steps that are compatible with python.

3/ Try to mimic the style/tone of the question in your answers to best-match potential knowledge levels.

4/ Responses should be very similar or even identical to the past good answers, 
in terms of length, ton of voice, logical arguments and other details

5/ Responses can only be about Python. If you think the question is too irrelevant to Python, then you
need to find a way to relate it to Python or tell the user that this forum is only used for Python
questions.

6/ If a question seems too vague, find ways to tie it into the Python topic and suggest examples of
more specific questions they could ask.

Below is a question posted to the forum:
{question}

Here is a list of similar answers posted to the forum for similar situations:
{good_answers}

Please write the best answer that will be posted as a reply to the question.

"""

prompt = PromptTemplate(
    input_variables=["question", "good_answers"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)


# --------------------------------------
# Step 5: Retrieval augmented generation
# --------------------------------------

def generate_response(question):
    good_answers = retrieve_info(question)
    answer = chain.run(question=question, good_answers=good_answers)
    return answer

question = """

I have an AWS EC2 instance. Can I get details about it?

"""

answer = generate_response(question)
print(answer)

# --------------------------------------------------------
# Step 6: Build an app with streamlit (so we can share it)
# --------------------------------------------------------

def main():
    st.set_page_config(
        page_title="Python Advice Generator", page_icon=":bird:")

    st.header("Python Advice Generator :bird:")
    question = st.text_area("User Question")

    if question:
        st.write("Generating Python Advice...")

        answer = generate_response(question)

        st.info(answer)

if __name__ == '__main__':
    main()
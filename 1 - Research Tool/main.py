import os
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env

st.title("Research tool")
st.sidebar.title("Article URLs")

if 'embeddings' not in st.session_state:
    st.session_state.embeddings = None
#embeddings = None

urls = []
for i in range(1):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Load URLs")
llm = OpenAI(temperature=0.9, max_tokens=500)

file_path = "embeddings.pkl"

placeholder = st.empty()

if process_url_clicked:
    placeholder.text('[#------] Loading Data... ')
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ' '],
        chunk_size=500
    )
    placeholder.text('[##-----] Splitting Data... ')
    docs = text_splitter.split_documents(data)

    placeholder.text('[###----] Building embedding vector... ')
    st.session_state.embeddings = OpenAIEmbeddings()
    placeholder.text('[#####--] Embedding vector built. ')
    vector_index = FAISS.from_documents(docs, st.session_state.embeddings)
    placeholder.text('[######-] Saving vectors... ')
    vector_index.save_local("faiss_index_dir")
    placeholder.text('[#######] Finishing... ')


query = placeholder.text_input("Question: ")

if query:
    if os.path.exists('faiss_index_dir/index.faiss'):
        loaded_vector_index = FAISS.load_local("faiss_index_dir", st.session_state.embeddings, allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=loaded_vector_index.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        st.header("Answer")
        st.write(result['answer'])

        sources = result.get('sources', "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split('\n')
            for source in sources_list:
                st.write(source)















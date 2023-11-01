
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

class ChunksExtraction:

    def get_Vectorstore(self,VdbPath):
        #embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2',
                                #model_kwargs = {"device" : "cpu"})
        embeddings = OpenAIEmbeddings(openai_api_key='')

        vectorstore = FAISS.load_local(VdbPath, embeddings)
        return vectorstore
    
    def get_chunks(self,vectorstore,question):
        retriever = vectorstore.as_retriever(search_kwargs={"k": 8})
        docs = retriever.get_relevant_documents(question)
        return docs
    

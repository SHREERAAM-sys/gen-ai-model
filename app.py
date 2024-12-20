import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import Together
from langchain.chains import LLMChain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os



# ============ USER CONFIG SECTION ============
# Set your vector database path here
VECTOR_DB_PATH = "./vectordb/oci_security_db"  # User should modify this

# Set your Together.ai API key here
#TOGETHER_API_KEY = "" # User should modify this
# =============================================

load_dotenv(dotenv_path="./.env")

# Set the API key for Together.ai
#os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

embeddings = HuggingFaceEmbeddings()

def initialize_vectordb():
    if not VECTOR_DB_PATH:
        return None
    else:
        vectordb = Chroma(collection_name="text_collection",persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)
        return vectordb
    
    #TODO Create code for loading vector database 
    

def get_context(query, vectordb=None):
    if vectordb is None:
        return ""
    
    #TODO Create code for completing semantic search on vectordb


    docs = vectordb.similarity_search(query, k=10)  # retrieving top 10 chunks by doing similarity search
    context = "\n".join([doc.page_content for doc in docs])
    return context
    

def main():
    st.title("OCI Security Services")
    
    vectordb = initialize_vectordb()
    
    if vectordb:
        st.info("Vector database loaded successfully! Using contextual responses.")
    else:
        st.info("No vector database configured. The assistant will provide general responses.")
    
    
    query = st.text_input("Enter your question about OCI security services:")
    
    if query:

        context = get_context(query, vectordb) if vectordb else ""

        st.session_state.history.append({"role": "user", "content": query})
        
        
        if context:
            with st.expander("View Retrieved Context"):
                st.markdown(context)

        try:
            
            llm = Together(
                model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                max_tokens=500
            )
            
            
            if context:
                #TODO Once added chroma db, modify this prompt template 
                prompt = PromptTemplate(
                    template="""
                    System Message: Your response will be concise and straight to the point. It will end as a statement
                    Context:
                    {context}
            
                    Question: {question}
                    """,
                    input_variables=["context", "question"]
                )
            else:
                prompt = PromptTemplate(
                    template="""
                    
                    Question: {question}

                    Answer:""",
                    input_variables=["question"]
                )
            
         
            chain = LLMChain(llm=llm, prompt=prompt)
            response = chain.run(
                context=context if context else "",
                question=query
            )
            
            
            st.markdown("### Answer")
            st.markdown(response)
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")

if __name__ == "__main__":
    main()

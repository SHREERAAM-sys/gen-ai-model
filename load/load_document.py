from uuid import uuid4

from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import MarkdownTextSplitter
from langchain_chroma import Chroma


def create_vector_db(file_path: str, persist_directory: str):
    #TODO Add code to chunk and embed document

    """
       Reads a document, chunks it, and embeds it into a vector database.
    """

    embeddings = HuggingFaceEmbeddings()
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    markdown_splitter = MarkdownTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = markdown_splitter.create_documents([markdown_text])

    vector_store = Chroma(
        collection_name="text_collection",
        embedding_function=embeddings,
        persist_directory=persist_directory,
    )
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(documents=docs, ids=uuids)
    print(f"Vector database successfully created and persisted at {persist_directory}")
    return



def open_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def main():
    # Set up paths
    input_file = "../docs/oci_security.md"
    
    persist_dir = "../vectordb/oci_security_db"
    
    # Create vector database
    vectordb = create_vector_db(input_file, persist_dir)
    
    print(f"Successfully created vector database at {persist_dir}")
    
    

if __name__ == "__main__":
    main()
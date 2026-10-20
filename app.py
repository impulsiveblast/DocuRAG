from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.vectorstores import InMemoryVectorStore
from time import sleep
import streamlit as st
# 1. Load PDF

api_key = st.secrets["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0,
    google_api_key=api_key,
)

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "messages" not in st.session_state:
    st.session_state.messages = []

def document_process(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    # print("Total pages:", len(docs))

    # 2. Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)
    print("Number of chunks created:", len(chunks))

    # 3. Create Gemini embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        google_api_key=api_key
    )

    # 4. Create vector store
    vectorstore = InMemoryVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings
        )
    st.session_state.vector_db = vectorstore
    st.session_state.document_uploaded = True




    # 5. Search for relevant chunks
#     query = "What is the age of the patient?"

#     documents = vectorstore.similarity_search(
#         query=query,
#         k=2
#     )

# context = ""

# for doc in documents:
#     context += doc.page_content + "\n"

# # 6. Prepare prompt
# prompt = f"""
# You are a helpful assistant answering questions about a medical report.

# Answer using only the context below.
# If the answer is unavailable, say:
# "It isn't available in the given document."

# Context:
# {context}

# Question:
# {query}
# """

# # 7. Generate answer using Gemini


# answer = llm.invoke(prompt)

# print("Answer:", answer.content)




###UI CREATION

#Header

st.subheader("📄 DocuRAG")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

#### document upload
if not st.session_state.document_uploaded:
    file = st.file_uploader(label="Select Your PDF File", type="pdf")
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())

        with st.spinner("Processing..."):
            document_process("./uploaded_document.pdf")

        st.markdown("Document Processed Successfully...")
        sleep(2)
        st.rerun()


if st.session_state.document_uploaded and st.session_state.vector_db:
        query = st.chat_input("Ask Anything...")

        for onemessage in st.session_state.messages:
            if onemessage["role"] == "user":
                st.chat_message("user").markdown(onemessage["content"])
            else:
                st.chat_message("assistant").markdown(onemessage["content"])

        if query:
            
            #list,tuple or dictionary can be used to store messages in session state

            st.session_state.messages.append({"role": "user", "content": query})
            st.chat_message("user").markdown(query)
            documents = st.session_state.vector_db.similarity_search(query, k=2)
            context = ""

            for doc in documents:
                context += doc.page_content + "\n\n"

            prompt = f"""You are a helpful assistant and you provide answers based on the context provided below: {context} tell me the answer to the following question: {query}
            Rules:
            - Give only the answer to the question.
            - Do not include metadata, token counts, model information,
            source object details, or technical explanations.
            """

            result=llm.invoke(prompt)

            st.session_state.messages.append({"role": "ai", "content": result.content[0]["text"]})
            st.chat_message("assistant").markdown(result.content[0]["text"])

            

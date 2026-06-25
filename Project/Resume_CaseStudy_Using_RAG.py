import streamlit as st
import chromadb
import tempfile
import json
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings
from langchain_openai import ChatOpenAI

load_dotenv()


# CHROMA DB


db = chromadb.PersistentClient(path="./knowledge_base")
collection = db.get_or_create_collection("resumes")


# EMBEDDING MODEL


embed_model = init_embeddings(
    model="text-embedding-nomic-embed-text-v1.5",
    provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="not-needed",
    check_embedding_ctx_length=False
)


# LLM


llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="qwen3-4b-2507"
)


# PDF LOADER


def load_resume(pdf_path):

    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    text = ""

    for page in pages:
        text += page.page_content + "\n"

    return text



# STORE RESUME


def store_resume(pdf_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(pdf_file.getvalue())
        pdf_path = tmp.name

    resume_id = Path(pdf_file.name).stem

    resume_text = load_resume(pdf_path)

    embedding = embed_model.embed_documents(
        [resume_text]
    )

    collection.add(
        ids=[resume_id],
        embeddings=embedding,
        documents=[resume_text],
        metadatas=[{
            "resume_id": resume_id,
            "file_name": pdf_file.name
        }]
    )

    return resume_id



# UI


st.set_page_config(
    page_title="AI Resume Screening",
    layout="wide"
)

st.title("AI Resume Screening Assistant")


# MULTIPLE FILE UPLOAD


uploaded_files = st.file_uploader(
    "Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Generate Knowledge Base"):

        progress = st.progress(0)

        total = len(uploaded_files)

        for i, file in enumerate(uploaded_files):

            try:
                resume_id = store_resume(file)

                st.success(
                    f"{resume_id} stored successfully"
                )

            except Exception as e:
                st.error(
                    f"Error processing {file.name}"
                )
                st.exception(e)

            progress.progress(
                (i + 1) / total
            )

        st.success(
            "Knowledge Base Generated Successfully"
        )

# KNOWLEDGE BASE INFO


st.divider()

all_ids = collection.get()["ids"]

st.metric(
    "Total Resumes In Knowledge Base",
    len(all_ids)
)


# ASK QUESTIONS


st.subheader("Ask HR Questions")

question = st.chat_input(
    "Example: Find Java developers with 3+ years experience"
)

if question:

    st.chat_message("user").write(question)

    query_embedding = embed_model.embed_query(
        question
    )

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    prompt = f"""
You are an experienced HR recruiter.

Question:
{question}

Retrieved Resumes:
{json.dumps(results)}

Instructions:

1. Analyze only retrieved resumes.
2. Select best candidates.
3. Mention:
   - Candidate Name
   - Skills
   - Experience
   - Resume ID
4. Explain why selected.
5. Rank candidates.
6. Do not hallucinate.

Provide output in a clean table.
"""

    response = llm.invoke(prompt)

    st.chat_message("assistant").write(
        response.content
    )
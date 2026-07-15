import requests
import streamlit as st

st.set_page_config(
    page_title="RAG PDF Question Answering",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 RAG PDF Question Answering System")

st.caption(
    "Ask questions from your documents using LangChain + FAISS + Llama 3.1"
)
st.markdown(
    "Upload a PDF document and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📤 Upload PDF")

    uploaded_file = st.sidebar.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    upload_button = st.sidebar.button(
        "📤 Upload PDF"
    )

    if upload_button:

        if uploaded_file is None:
            st.warning("Please select a PDF file.")

        else:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

        with st.spinner("Processing PDF and creating embeddings..."):


            response = requests.post(
                "http://127.0.0.1:8000/upload",
                files=files
            )

            if response.status_code == 200:
                st.success("PDF uploaded successfully ✅")
                st.json(response.json())

            else:
                st.error("Upload failed.")

with col2:
    st.subheader("💬 Ask Question")

    question = st.text_area(
        "Enter your question"
    )

    ask_button = st.button("Ask")

    if ask_button:

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            payload = {
                "question": question
            }

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Answer Generated Successfully ✅")

                st.subheader("🤖 Answer")

                st.success("Answer Generated Successfully ✅")

                st.info(
                    data["response"]["answer"]
                )

                st.subheader("📚 Sources")

                for source in data["response"]["sources"]:

                    with st.expander(
                        f"📄 {source['file']} | Page {source['page']}"
                    ):

                        st.write(
                            source["content"]
                        )


                    st.markdown(
                        f"""
    **📄 File:** {source['file']}

    **📃 Page:** {source['page']}

    **Snippet:**

    {source['content']}

    ---
    """
                    )

            else:

                st.error("Unable to generate answer.")



st.divider()


st.subheader("🤖 Answer")

st.info("Answer will appear here.")

st.subheader("📚 Sources")

st.info("Sources will appear here.")

st.caption(
    "Built with FastAPI • LangChain • FAISS • Ollama • Streamlit"
    
)
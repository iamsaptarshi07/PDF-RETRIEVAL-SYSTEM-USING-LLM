import streamlit as st


def main():
    st.set_page_config("Information Retrieval")
    st.header("PDF-Information-Retrieval-System")

    with st.sidebar:
        st.title("PDF Upload")
        pdf_files = st.file_uploader(
            "Upload PDF Files and click Submit", accept_multiple_files=True
        )
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                st.success("Done")


if __name__ == "__main__":
    main()

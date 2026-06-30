import streamlit as st
import google.generativeai as genai
import PyPDF2
st.set_page_config(page_title="GATE CSE AI Coach", layout="wide")
st.title(" GATE CSE AI Coach")
st.caption("Built for GATE CSE Aspirant")

# API Key from Stremlit Secrets
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Sidebar
st.sidebar.header(" Tools")
option = st.sidebar.selectbox("Choose Tool", ["Doubt Pucho", "MCQ Generator", "PDF Notes"])

if option == "Doubt Pucho":
   st.subheader("Ask Any GATE CSE Doubt")
   query = st.text_input("Ex: Explain OS Paging in Hindi")
   if st.button("Ask AI") and query:
        with st.spinner("Socho mtt..")
             promt = f"You are a GATE CSE expert. Explain In simple Hindi + English mix: {query}"
             response = model.generate_content(prompt)
             st.success(response.text)

elif option == "MCQ Generator":
    st.subheader("Generate GATE Level MCQ")
    topic = st.text_input("Enter Topic: EX:DBMS Normalization")
    if st.button("Generate MCQ") and topic:
        with st.spinner("MCQ Generater HO Rhe H"):
            prompt = f"Create 1 GATE CSE level MCQ on {topic} with 4 options, answer, and explanation in 2 lines."
            response = model.generate_content(prompt)
            st.write(response.text)

elif option == "PDF Notes":
     st.subheader("Upload PDF Notes")
     uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
     if uploaded_file and st.button("Summarize"):
         with st.spinner("Notes Ban Rhe H..")
              pdf_reader = PyPDF2.PdfReader(uploaded_file)
              text = "".join(page.extract_text() for page in pdf_reader.pages)
              prompt = f"Summarize this GATE CSE notes in 5 bullet points in Hindi: {text[:4000]}"
              response = model.generate_content(prompt)
              st.success(response.text)

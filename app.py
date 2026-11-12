import streamlit as st
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Tata Group AI Legal Document Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main-header { font-size: 2.5rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; }
    .sub-header { font-size: 1.1rem; color: #6B7280; margin-bottom: 30px; }
    .stButton>button { width: 100%; border-radius: 5px; }
    .doc-status { background-color: #DBEAFE; color: #1E3A8A; padding: 10px; border-radius: 5px; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Document Hub ---
with st.sidebar:
    st.markdown("### 📁 Document Hub")
    st.markdown("**Upload Legal File**")
    
    uploaded_file = st.file_uploader(
        label="Upload", 
        type=['txt', 'pdf', 'docx', 'csv'],
        help="200MB per file • TXT, PDF, DOCX, CSV",
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.markdown("### 📄 Available Documents")
    if uploaded_file is not None:
        st.markdown(f'<div class="doc-status">System Ready. <b>{uploaded_file.name}</b> active.</div>', unsafe_allow_html=True)
        active_doc_name = uploaded_file.name
    else:
        # Mock active document for demonstration matching the image
        st.markdown('<div class="doc-status">System Ready. <b>legal_nda.txt</b> active.</div>', unsafe_allow_html=True)
        active_doc_name = "legal_nda.txt"

# --- Main Layout ---
st.markdown('<div class="main-header">⚖️ Tata Group AI Legal Document Intelligence System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Enterprise-Grade Multi-Document RAG & Automated Legal Audit Assistant</div>', unsafe_allow_html=True)

st.markdown("### 🚀 Pre-built Legal Audits & Smart Chat")

# Document Selector
st.markdown("Select Document to Analyze:")
selected_doc = st.selectbox(
    "Select Document",
    options=["1", active_doc_name, "All Knowledge Base Documents"],
    label_visibility="collapsed"
)

# Action Buttons row
col1, col2, col3 = st.columns(3)
with col1:
    btn_summarize = st.button("🔍 Summarize Agreement")
with col2:
    btn_detect = st.button("⚠️ Detect Hidden Risks")
with col3:
    btn_extract = st.button("🗓️ Extract Deadlines/Terms")

st.divider()

# Smart Chat Interface
st.markdown("#### Chat with Document Context")
chat_query = st.chat_input("Ask a question about the selected document...")

# Logic Placeholders
if btn_summarize:
    st.info(f"Generating summary for {selected_doc}...")
    # Add backend API call here
if btn_detect:
    st.warning(f"Analyzing {selected_doc} for compliance and hidden liabilities...")
    # Add backend API call here
if btn_extract:
    st.success(f"Extracting key dates and financial terms from {selected_doc}...")
    # Add backend API call here

if chat_query:
    st.chat_message("user").write(chat_query)
    st.chat_message("assistant").write(f"I am analyzing the legal context to answer: '{chat_query}'")
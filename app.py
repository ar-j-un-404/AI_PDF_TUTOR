import streamlit as st
import importlib
from ai_engine import get_answer

st.set_page_config(
    page_title="AI PDF Tutor",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI PDF Tutor")

if st.button("🔄 Reload PDF"):
    import ai_engine
    importlib.reload(ai_engine)
    st.success("✅ PDF reloaded successfully!")
    st.rerun()

st.markdown("---")

question = st.text_input("Ask a question about the PDF:")

if question:
    with st.spinner("🤔 Searching PDF and generating answer..."):
        answer = get_answer(question)
    
    st.markdown("### 📖 Answer:")
    st.write(answer)
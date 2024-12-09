import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

st.title("Teks Summarization App")
st.markdown("""
Aplikasi ini meringkas teks secara otomatis menggunakan teknologi AI berbasis model BART. 
Hasil ringkasan akan berupa kalimat baru yang mempertahankan makna teks asli.
""")

user_input = st.text_area("Masukkan teks di bawah ini:", height=300)

if st.button("Ringkas Teks"):
    if user_input.strip():
        with st.spinner("Sedang meringkas teks..."):
            try:
                summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
                st.success("Ringkasan berhasil dibuat:")
                st.write(summary[0]['summary_text'])
            except Exception as e:
                st.error(f"Terjadi kesalahan saat meringkas teks: {e}")
    else:
        st.error("Masukkan teks terlebih dahulu untuk diringkas.")

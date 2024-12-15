import streamlit as st
import csv
from langdetect import detect, detect_langs

def load_language_mapping(file_path):
    mapping = {}
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                mapping[row["ISO_code"]] = row["Language"]
    except Exception as e:
        st.error(f"Failed to load language mapping: {str(e)}")
    return mapping

def get_language_name(code, mapping):
    return mapping.get(code, code) 

def identify_language_langdetect(text):
    try:
        lang = detect(text)
        probabilities = detect_langs(text)
        return lang, probabilities
    except Exception as e:
        return None, f"Error: {str(e)}"

LANGUAGE_MAPPING = load_language_mapping("ISO_639-1_LanguageCodes.csv")

st.title("Language Identifier")
st.write("Enter a text snippet, and this app will identify its language.")

text = st.text_area("Enter your text here:", "")

if st.button("Identify Language"):
    if text.strip():
        st.write("### Results:")
        lang_detect, probabilities = identify_language_langdetect(text)
        if lang_detect:
            lang_name = get_language_name(lang_detect, LANGUAGE_MAPPING)
            st.write(f"**Detected Language:** {lang_name} ({lang_detect})")
            
            st.write("**Probabilities:**")
            for prob in probabilities:
                code = str(prob.lang)
                prob_lang_name = get_language_name(code, LANGUAGE_MAPPING)
                st.write(f"- {prob_lang_name} ({code}): {prob.prob:.2%}")
        else:
            st.error(f"Error: {probabilities}")
    else:
        st.warning("Please enter some text to identify.")

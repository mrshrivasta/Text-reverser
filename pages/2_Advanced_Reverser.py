import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.reverser import *

st.set_page_config(page_title="Professional & Smart Reverser", page_icon="🧠")

st.title("🧠 Professional & Smart Reverser")
st.write("Context-aware reversal for code, technical text, and structured data.")

input_text = st.text_area("Enter technical text (Code, URLs, HTML, etc.):", height=200)

smart_mode = st.radio("Smart Reversal Category:", [
    "Safe URL Reversal (Keeps URLs intact)",
    "Safe HTML Reversal (Keeps tags intact)",
    "CamelCase Reversal",
    "snake_case Reversal",
    "kebab-case Reversal",
    "Inside Brackets Only",
    "Hashtags Only",
    "Mentions Only",
    "Preserve Capitalization Positions"
])

def process_smart(text, mode):
    if not text: return ""

    if "URL" in mode: return reverse_urls_safely(text)
    if "HTML" in mode: return reverse_preserving_html(text)
    if "CamelCase" in mode: return reverse_camel_case(text)
    if "snake_case" in mode: return reverse_snake_case(text)
    if "kebab-case" in mode: return reverse_kebab_case(text)
    if "Brackets" in mode: return reverse_inside_brackets(text)
    if "Hashtags" in mode: return reverse_hashtags_only(text)
    if "Mentions" in mode: return reverse_mentions_only(text)
    if "Capitalization" in mode: return reverse_preserving_capitalization(text)
    return text

output_text = process_smart(input_text, smart_mode)

st.subheader("Smart Output:")
st.code(output_text, language="python")

with st.expander("Usage Tips"):
    st.info("""
    - **Safe URL**: Useful when you want to reverse a paragraph but keep links clickable.
    - **Safe HTML**: Keeps your <div> and <span> tags working while reversing the content.
    - **Brackets Only**: Great for reversing logic inside code blocks without breaking the structure.
    """)

if st.button("Download JSON Output"):
    import json
    data = {"original": input_text, "mode": smart_mode, "reversed": output_text}
    st.download_button(
        "Download JSON",
        data=json.dumps(data, indent=2),
        file_name="smart_reverse.json",
        mime="application/json"
    )

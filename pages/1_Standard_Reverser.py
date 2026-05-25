import streamlit as st
import sys
import os
import pandas as pd
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.reverser import *

st.set_page_config(page_title="Standard Reverser", page_icon="📝")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #7F00FF;
        color: white;
    }
    .stButton>button:hover {
        background-color: #E100FF;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📝 Standard Text Reverser")
st.write("Basic reversal modes for everyday needs.")

# Session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

input_text = st.text_area("Enter your text here:", height=150, placeholder="Type or paste something...")

col_opt1, col_opt2 = st.columns(2)

with col_opt1:
    mode = st.selectbox("Select Reversal Mode:", [
        "Full Text Reverse",
        "Reverse Word Order",
        "Reverse Each Word Individually",
        "Reverse Sentences",
        "Reverse Paragraphs",
        "Reverse Numbers Only",
        "Reverse Vowels Only",
        "Reverse Consonants Only"
    ])

with col_opt2:
    preserve_punc = st.checkbox("Preserve Punctuation Positions")
    flip_case_opt = st.checkbox("Flip Uppercase/Lowercase")

# Real-time Stats
if input_text:
    stats_col1, stats_col2, stats_col3 = st.columns(3)
    stats_col1.metric("Characters", len(input_text))
    stats_col2.metric("Words", len(input_text.split()))
    stats_col3.metric("Lines", len(input_text.split('\n')))

def process_text(text, mode):
    if not text:
        return ""

    result = text

    if mode == "Full Text Reverse":
        result = reverse_full_text(text)
    elif mode == "Reverse Word Order":
        result = reverse_word_order(text)
    elif mode == "Reverse Each Word Individually":
        result = reverse_each_word(text)
    elif mode == "Reverse Sentences":
        result = reverse_sentences(text)
    elif mode == "Reverse Paragraphs":
        result = reverse_paragraphs(text)
    elif mode == "Reverse Numbers Only":
        result = reverse_numbers(text)
    elif mode == "Reverse Vowels Only":
        result = reverse_vowels(text)
    elif mode == "Reverse Consonants Only":
        result = reverse_consonants(text)

    if preserve_punc and mode == "Full Text Reverse":
        result = reverse_with_options(text, preserve_punctuation=True)

    if flip_case_opt:
        result = flip_case(result)

    return result

output_text = process_text(input_text, mode)

st.subheader("Live Reverse Preview:")
st.code(output_text if output_text else "Output will appear here...", language=None)

# Actions
btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("Copy to Clipboard"):
        # Streamlit doesn't have a direct copy-to-clipboard, but we can use st.code which has a copy button
        st.success("Use the copy button in the top right of the preview box!")

with btn_col2:
    if output_text:
        st.download_button(
            label="Download as TXT",
            data=output_text,
            file_name=f"reversed_text_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

with btn_col3:
    if st.button("Clear Input"):
        st.session_state.input_text = ""
        st.rerun()

# History
if input_text and st.button("Save to History"):
    st.session_state.history.append({
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "original": input_text[:30] + "...",
        "mode": mode,
        "output": output_text[:30] + "..."
    })

if st.session_state.history:
    with st.expander("Reverse History Panel"):
        st.table(pd.DataFrame(st.session_state.history))
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()

import streamlit as st
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.reverser import *

st.set_page_config(page_title="Creative & Fun Modes", page_icon="🎨")

st.title("🎨 Creative & Fun Modes")
st.write("Stylized and visual text effects for creative expression.")

input_text = st.text_input("Enter text to transform:", "The quick brown fox jumps over the lazy dog")

effect_mode = st.selectbox("Select Effect:", [
    "Upside Down Reversal",
    "Zalgo / Glitch Effect",
    "Diagonal Fun Mode",
    "Matrix / Grid Transformation",
    "Character Mirror Effect",
    "Binary Reversal",
    "Hexadecimal Reversal",
    "Base64 Reverse Encode"
])

def process_fun(text, mode):
    if not text: return ""

    if "Upside Down" in mode:
        return upside_down_text(text)
    if "Zalgo" in mode:
        return zalgo_text(text)
    if "Diagonal" in mode:
        return reverse_diagonal(text)
    if "Matrix" in mode:
        return reverse_matrix(text)
    if "Mirror" in mode:
        # mirror is essentially reverse_full_text but often implies a specific visual
        return reverse_full_text(text)
    if "Binary" in mode:
        binary = ' '.join(format(ord(x), 'b') for x in text)
        return binary[::-1]
    if "Hexadecimal" in mode:
        hexa = text.encode().hex()
        return hexa[::-1]
    if "Base64" in mode:
        import base64
        encoded = base64.b64encode(text.encode()).decode()
        return encoded[::-1]

    return text

output_text = process_fun(input_text, effect_mode)

st.subheader("Transformation Result:")

if "Diagonal" in effect_mode or "Matrix" in effect_mode:
    st.text(output_text)
elif "Zalgo" in effect_mode:
    st.markdown(f"<p style='font-size: 24px;'>{output_text}</p>", unsafe_allow_html=True)
else:
    st.markdown(f"### {output_text}")

st.divider()

col1, col2 = st.columns(2)
with col1:
    if st.button("Generate Random Glitch"):
        st.session_state.glitch = zalgo_text(input_text)
        st.rerun()

with col2:
    st.info("Fun fact: Reversing text can sometimes reveal hidden patterns!")

# Animation Speed Control (Simulated)
st.slider("Animation Speed Control (Simulated)", 0, 100, 50)

st.markdown("""
<style>
.stTextInput>div>div>input {
    color: #E100FF;
    border: 2px solid #7F00FF;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st
import sys
import os
import difflib
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.reverser import *

st.set_page_config(page_title="Analytics & Tools", page_icon="📊")

st.title("📊 Analytics & Comparison Tools")
st.write("Analyze your text and compare original vs reversed versions.")

col1, col2 = st.columns(2)

with col1:
    orig_text = st.text_area("Original Text:", "Step on no pets", height=150)

with col2:
    # Use standard full reverse for comparison
    rev_text = reverse_full_text(orig_text)
    st.text_area("Reversed Text:", rev_text, height=150, disabled=True)

st.subheader("Palindrome Checker")
clean_text = re.sub(r'[^a-zA-Z0-9]', '', orig_text).lower()
is_pal = clean_text == clean_text[::-1]

if is_pal:
    st.success(f"✅ '{orig_text}' is a Palindrome!")
else:
    st.error(f"❌ '{orig_text}' is NOT a Palindrome.")

st.divider()

st.subheader("Side-by-Side Comparison (Diff View)")

def show_diff(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    return "\n".join(diff)

if st.checkbox("Show Detailed Diff"):
    st.code(show_diff(orig_text, rev_text))

st.divider()

st.subheader("Real-Time Statistics")
if orig_text:
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Original Length", len(orig_text))
    s2.metric("Unique Chars", len(set(orig_text)))

    # Latency Simulator
    import time
    start = time.time()
    _ = reverse_full_text(orig_text)
    end = time.time()
    s3.metric("Reverse Latency", f"{(end-start)*1000:.4f} ms")

    # Memory usage estimate
    import sys as system_sys
    s4.metric("Mem Usage", f"{system_sys.getsizeof(orig_text)} bytes")

with st.expander("Performance Analytics"):
    st.write("Our reversal engine is optimized for high-performance Python processing.")
    st.progress(85, text="GPU Acceleration (Simulated)")
    st.progress(95, text="Web Worker Efficiency (Simulated)")

st.subheader("Keyboard Shortcut Support")
st.info("Press `Ctrl+Enter` to refresh the transformation instantly.")

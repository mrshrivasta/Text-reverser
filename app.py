import streamlit as st
import os

# Custom CSS for the specified colors
st.set_page_config(
    page_title="Ultimate Text Reverser | Professional Suite",
    page_icon="🔄",
    layout="wide",
)

st.markdown(f"""
    <style>
    .main {{
        background-color: #0E1117;
    }}
    .stButton>button {{
        background-color: #7F00FF;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #E100FF;
        color: white;
    }}
    h1, h2, h3 {{
        color: #E100FF !important;
    }}
    .sidebar .sidebar-content {{
        background-image: linear-gradient(#7F00FF, #E100FF);
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("🔄 Ultimate Text Reverser")
st.subheader("The Most Powerful Text Transformation Suite Built with Python")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🚀 Transform Your Text in Seconds
    Welcome to the ultimate utility for text reversal and styling. Whether you are a developer, a content creator, or just looking for some fun, we have everything you need.

    ### 🛠️ Key Modules:
    - **Standard Reverser**: Quick and simple reversal modes.
    - **Advanced & Smart**: Context-aware transformations for code, URLs, and HTML.
    - **Creative & Fun**: Glitch, upside-down, and matrix effects.
    - **Analytics & Tools**: Compare, track history, and check palindromes.
    - **SEO & Insights**: Learn about modern SEO (GEO, AEO, AIO, SXO).

    ### 💎 Features:
    - ⚡ **Live Preview**: See changes instantly as you type.
    - 💾 **Export Options**: Download as TXT, JSON, or CSV.
    - 🌓 **Themed UI**: Modern dark mode with neon accents.
    - 📱 **Mobile Friendly**: Works perfectly on all devices.
    """)

with col2:
    st.image("https://img.icons8.com/clouds/200/000000/re-order.png", width=200)
    st.info("👈 Use the sidebar to select a specific toolset!")

    with st.expander("Why use Text Reverser?"):
        st.write("""
        - Data obfuscation
        - Creative social media posts
        - Testing string manipulation in code
        - Solving puzzles and riddles
        - Just for fun!
        """)

st.divider()

st.markdown("""
<div style='text-align: center; color: #7F00FF;'>
    Built with ❤️ by <a href='https://github.com/mrshrivasta' style='color: #E100FF;'>mrshrivasta</a>
</div>
""", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(page_title="SEO & Insights", page_icon="📈")

st.title("📈 SEO & Search Evolution Insights")
st.write("Understand the future of search and content discovery.")

# Add search optimization concepts
tabs = st.tabs(["SEO", "GEO", "AEO", "AIO", "SXO"])

with tabs[0]:
    st.header("SEO (Search Engine Optimization)")
    st.write("The foundation of being found on Google and other search engines. Focuses on keywords, backlinks, and technical health.")

with tabs[1]:
    st.header("GEO (Generative Engine Optimization)")
    st.write("The new frontier. Optimizing content to be cited by Generative AI models like Perplexity, ChatGPT, and Gemini.")

with tabs[2]:
    st.header("AEO (Answer Engine Optimization)")
    st.write("Optimizing for voice search and direct answers (Featured Snippets). Being the 'single source of truth'.")

with tabs[3]:
    st.header("AIO (AI Overview Optimization)")
    st.write("Strategies to appear in Google's AI Overviews by providing concise, high-value summaries.")

with tabs[4]:
    st.header("SXO (Search Experience Optimization)")
    st.write("The intersection of SEO and UX. Ensuring that once a user finds you, their experience is flawless.")

st.divider()

st.warning("### ⚠️ STRONG DISCLAIMER / HUMAN VERIFICATION")
st.markdown("""
**THIS TOOL IS FOR EDUCATIONAL AND CREATIVE PURPOSES ONLY.**
- Reversing text may obfuscate meaning but is **NOT** a replacement for strong encryption (AES, etc.).
- Do not use this tool for sensitive data storage.
- All processing is done **LOCALLY** in your browser session; no data is sent to our servers.
- **Human Verification**: Users are responsible for verifying the output before use in critical applications.
""")

st.divider()

st.subheader("👨‍💻 Developer & Contact")
st.markdown("""
- **LinkedIn**: [Karanam Shrivasta](https://www.linkedin.com/in/karanam-shrivasta/)
- **GitHub**: [mrshrivasta](https://github.com/mrshrivasta)
- **Portfolio**: [Visit mrshrivasta's GitHub](https://github.com/mrshrivasta)
""")

st.divider()

st.markdown("""
### Additional Features
- **Offline Support (PWA)**: This app can be cached for offline use.
- **Privacy Mode**: Temporary data is cleaned automatically upon session end.
- **Secure Processing**: API-free local processing ensures your text stays yours.
""")

st.info("Built with 100% Python for the community.")

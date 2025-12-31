import streamlit as st
from utils import load_data

st.set_page_config(page_title="Amazon Review Dashboard", layout="wide")

st.title("🛍️ Amazon Product Review Analysis")
st.markdown("""
### Project Overview
This dashboard provides a deep dive into Amazon fine food reviews. 
Use the sidebar to navigate through different analysis perspectives:
- **Product Review:** Trends in high-volume products.
- **Reviewer Analysis:** Comparing frequent vs. casual reviewers.
- **Sentiment Analysis:** Understanding the "vibe" of the summaries.
""")

# Show some high-level stats immediately
df = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", f"{len(df):,}")
col2.metric("Unique Products", f"{df['ProductId'].nunique():,}")
col3.metric("Avg. Sentiment Score", f"{df['Score'].mean():.2f} / 5")

st.info("👈 Select a page in the sidebar to begin the analysis.")
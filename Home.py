import streamlit as st
from utils import load_data

# Page Config
st.set_page_config(page_title="Amazon Review Dashboard", layout="wide", initial_sidebar_state="expanded")

# 1. Title and Introduction
st.title("🛍️ Amazon Product Review Analytics")
st.markdown("---")

# 2. Key Performance Indicators (KPIs)
# We place these in a high-visibility container at the top
df = load_data()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Reviews", f"{len(df):,}", help="Total number of reviews in the dataset")
with col2:
    st.metric("Unique Products", f"{df['ProductId'].nunique():,}")
with col3:
    st.metric("Avg. Rating", f"{df['Score'].mean():.2f} / 5", delta=f"{df['Score'].std():.2f} (std dev)",
              delta_color="off")
with col4:
    unique_users = df['UserId'].nunique()
    st.metric("Unique Reviewers", f"{unique_users:,}")

st.markdown("---")

# 3. Project Overview and Navigation Guide
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("🚀 Project Overview")
    st.write("""
    This interactive dashboard analyzes thousands of **Amazon Fine Food Reviews** to uncover patterns in consumer 
    behavior, product performance, and overall sentiment. By leveraging data science techniques, we 
    transform raw text and ratings into actionable insights.
    """)

    st.info("💡 **Getting Started:** Use the sidebar on the left to navigate between specific analysis modules.")

with right_col:
    st.subheader("📂 Analysis Modules")
    st.markdown("""
    - **📦 Product Review:** Identify high-volume products and their score distributions.
    - **👤 Reviewer Analysis:** Compare behaviors of frequent vs. casual contributors.
    - **🏆 Top Contributors:** Discover the most active users and volume trends.
    - **🧠 Sentiment Analysis:** Decode the emotional 'vibe' of textual summaries.
    """)

st.divider()

# 4. Quick Data Preview
with st.expander("📊 View Raw Dataset Preview"):
    st.write("Below is a sample of the underlying data being analyzed across all pages.")
    st.dataframe(df.head(10), use_container_width=True)

# 5. Footer
st.caption("Developed for the Amazon Review Analysis Project | © 2026")
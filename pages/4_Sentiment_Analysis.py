import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from textblob import TextBlob
from collections import Counter
import pandas as pd
from utils import load_data

st.set_page_config(layout="wide", page_title="Sentiment Analysis")

st.title("🧠 Sentiment Analysis")
df = load_data()

# 1. Sidebar/Top Controls
with st.expander("⚙️ Analysis Settings", expanded=True):
    sample_size = st.slider("Select sample size for analysis", 5000, 50000, 20000)
    run_btn = st.button("Run Analysis", use_container_width=True)

if run_btn:
    with st.spinner("Analyzing sentiment polarity..."):
        # Prepare Sample
        sample = df.sample(sample_size).copy()  # Use .sample() instead of .head() for better variety
        sample['polarity'] = sample['Summary'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        # --- SECTION 1: RELATIONSHIP ANALYSIS ---
        st.subheader("Sentiment Polarity vs. Star Rating")

        # Plotly Violin plot shows density better than a boxenplot
        fig_violin = px.violin(
            sample,
            x='Score',
            y='polarity',
            color='Score',
            box=True,
            points=False,
            color_discrete_sequence=px.colors.diverging.RdYlGn,
            template="plotly_white",
            height=500
        )

        fig_violin.update_layout(
            showlegend=False,
            xaxis_title="Star Rating (1-5)",
            yaxis_title="Sentiment Polarity (-1 to 1)",
            margin=dict(l=20, r=20, t=20, b=20)
        )

        st.plotly_chart(fig_violin, use_container_width=True)
        st.info(
            "💡 **Interpretation:** 5-star reviews should cluster toward 1.0 (Positive), while 1-star reviews should lean toward -1.0 (Negative).")

        st.divider()

        # --- SECTION 2: TOP PHRASES ---
        st.subheader("🗣️ Common Sentiment Phrases")

        pos_reviews = sample[sample['polarity'] > 0.5]  #
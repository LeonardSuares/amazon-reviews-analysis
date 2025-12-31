import streamlit as st
import matplotlib.pyplot as plt
from textblob import TextBlob
from collections import Counter
from utils import load_data

st.title("Sentiment Analysis")
df = load_data()

# Let the user choose the sample size so the app doesn't hang
sample_size = st.slider("Select sample size for analysis", 5000, 50000, 20000)

if st.button("Run Analysis"):
    with st.spinner("Calculating polarity..."):
        sample = df.head(sample_size).copy()

        # Applying your logic
        sample['polarity'] = sample['Summary'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        pos_reviews = sample[sample['polarity'] > 0]
        neg_reviews = sample[sample['polarity'] < 0]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Top Positive Phrases")
            pos_counts = Counter(pos_reviews['Summary']).most_common(10)
            st.table(pos_counts)

        with col2:
            st.subheader("Top Negative Phrases")
            neg_counts = Counter(neg_reviews['Summary']).most_common(10)
            st.table(neg_counts)

        # Revived your visualization idea
        fig, ax = plt.subplots()
        sample['polarity'].hist(bins=20, ax=ax, color='skyblue', edgecolor='black')
        ax.set_title("Distribution of Sentiment Polarity")
        st.pyplot(fig)
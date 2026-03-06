import streamlit as st
import plotly.express as px
import re
from utils import load_data

# Set layout to wide to match the first page
st.set_page_config(layout="wide", page_title="Reviewer Behavior Analysis")


# 1. Helper Function
def clean_review_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()


st.title("👤 Reviewer Behavior Analysis")

# 2. Data Preparation
df = load_data()

# Logic: Identify frequent reviewers
user_counts = df['UserId'].value_counts()
df['viewer_type'] = df['UserId'].apply(lambda x: "Frequent" if user_counts[x] > 50 else "Casual")

# Calculate word count
df['Word_Count'] = df['Text'].apply(lambda x: len(str(x).split(' ')))

# --- TOP STATS SECTION ---
col1, col2 = st.columns(2)
with col1:
    frequent_count = (df['viewer_type'] == "Frequent").sum()
    st.metric("Frequent Reviewers (>50)", f"{frequent_count:,}")
with col2:
    avg_len = df['Word_Count'].mean()
    st.metric("Overall Avg Word Count", f"{avg_len:.1f} words")

st.divider()

# 3. Interactive Boxplots (Replaces Matplotlib/Seaborn)
st.subheader("📏 Review Length Distribution")

# Using Plotly for a responsive, interactive boxplot
fig = px.box(
    df,
    x="viewer_type",
    y="Word_Count",
    color="viewer_type",
    points=False,  # Hides outliers to keep the chart clean; hover to see stats
    color_discrete_map={"Frequent": "#7eb0d5", "Casual": "#fd7f6f"},
    labels={"viewer_type": "Reviewer Type", "Word_Count": "Word Count"},
    height=450,
    template="plotly_white"
)

# Clean up axes and remove legend (redundant with X axis)
fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=10, b=10))
fig.update_yaxes(range=[0, 600])  # Keep consistent with your original zoom level

st.plotly_chart(fig, use_container_width=True)

st.info("💡 **Insight:** Frequent reviewers tend to have a more consistent review length compared to casual users.")

st.divider()

# 4. Sample Reviews Section (Improved UI)
st.subheader("📝 Sample Reviews by User Type")

# Put the selector and the result in columns to reduce vertical scrolling
ui_col, review_col = st.columns([1, 2])

with ui_col:
    type_choice = st.radio("Select Reviewer Type", ["Frequent", "Casual"], index=0)
    st.write("---")
    if st.button("🔄 Get New Random Sample"):
        # This button forces a rerun to get a new sample
        st.rerun()

with review_col:
    sample_df = df[df['viewer_type'] == type_choice]

    if not sample_df.empty:
        sample_review = sample_df.sample(1).iloc[0]
        cleaned_text = clean_review_text(sample_review['Text'])

        with st.container(border=True):  # Adds a subtle border around the review
            st.markdown(f"### Score: {sample_review['Score']}/5 ⭐")
            st.markdown(f"**Product ID:** `{sample_review['ProductId']}`")
            st.caption(f"Word Count: {len(cleaned_text.split())}")
            st.write(cleaned_text)
    else:
        st.warning("No data found for this category.")
import streamlit as st
import matplotlib.pyplot as plt
from utils import load_data

st.title("Top Contributing Users")
df = load_data()

# Aggregation logic
recommend_df = df.groupby(['UserId']).agg({
    'Summary': 'count',
    'Score': 'mean',
    'ProductId': 'count'
}).sort_values(by='ProductId', ascending=False)

recommend_df.columns = ['Total Reviews', 'Avg Score', 'Products Purchased']

st.subheader("Top 10 Most Active Reviewers")

# Visualization
fig, ax = plt.subplots(figsize=(12, 6))
top_10 = recommend_df.head(10)
ax.bar(top_10.index, top_10['Products Purchased'], color='teal')
ax.set_title('Top 10 Users by Product Count', fontsize=14)
plt.xticks(rotation=45)
st.pyplot(fig)

st.table(top_10)
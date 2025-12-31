import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.title("Product Review Analysis")

# 1. Load data using our central utility
df = load_data()

# 2. Logic to filter products with > 500 reviews
prod_count = df['ProductId'].value_counts().reset_index()
prod_count.columns = ['ProductId', 'count']
freq_prod_ids = prod_count[prod_count['count'] > 500]['ProductId'].values

# Filter main dataframe
freq_prod_df = df[df['ProductId'].isin(freq_prod_ids)]

st.subheader("Frequency of Products with Over 500 Reviews")

# 3. Visualization
fig, ax = plt.subplots(figsize=(10, 12))
sns.countplot(
    y='ProductId',
    data=freq_prod_df,
    hue='Score',
    order=freq_prod_df['ProductId'].value_counts().index,
    ax=ax
)
ax.set_title('Product Score Distribution (High Volume)', fontsize=16)
st.pyplot(fig)

# Added the "Nice to have" stats from your comments
st.write(f"**Total unique products before filtering:** {df['ProductId'].nunique()}")
st.write(f"**Total products reviewed more than 500 times:** {len(freq_prod_ids)}")
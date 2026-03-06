import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(layout="wide", page_title="Amazon Review Analysis")

st.title("📊 Product Review Analysis")

# 1. Load data
df = load_data()

# 2. Logic to filter products
prod_count = df['ProductId'].value_counts().reset_index()
prod_count.columns = ['ProductId', 'count']
freq_prod_ids = prod_count[prod_count['count'] > 500]['ProductId'].values
freq_prod_df = df[df['ProductId'].isin(freq_prod_ids)]

# --- KPI SECTION ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", f"{len(df):,}")
col2.metric("Unique Products", f"{df['ProductId'].nunique():,}")
col3.metric("High Volume (>500)", len(freq_prod_ids))

st.divider()

# 3. Main Horizontal Bar Chart (Plotly)
st.subheader("Frequency of High-Volume Products")

# Create the Plotly figure
fig = px.histogram(
    freq_prod_df,
    y="ProductId",
    color="Score",
    orientation='h',
    category_orders={"ProductId": freq_prod_df['ProductId'].value_counts().index.tolist()},
    color_discrete_sequence=px.colors.sequential.Plasma,
    height=500,  # Fixed height keeps it from getting "too long"
    template="plotly_white"
)

fig.update_layout(
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    yaxis_title="Product ID",
    xaxis_title="Number of Reviews"
)

# use_container_width=True makes it responsive to browser resizing
st.plotly_chart(fig, use_container_width=True)

st.divider()

# 4. Individual Product Lookup (Side-by-Side)
st.subheader("🔎 Individual Product Lookup")

search_col1, search_col2 = st.columns([1, 2])

with search_col1:
    selected_prod = st.selectbox("Select a Product ID", freq_prod_ids)
    prod_data = df[df['ProductId'] == selected_prod]

    avg_score = prod_data['Score'].mean()
    st.markdown(f"### Stats for `{selected_prod}`")
    st.write(f"**Average Rating:** {avg_score:.2f} ⭐")
    st.write(f"**Total Reviews:** {len(prod_data)}")

    # Simple table for top words or other small stats can go here

with search_col2:
    # Use a simple Bar chart for the specific product score distribution
    score_counts = prod_data['Score'].value_counts().reset_index()
    score_counts.columns = ['Score', 'Count']

    fig2 = px.bar(
        score_counts,
        x='Score',
        y='Count',
        color='Score',
        color_continuous_scale='Viridis',
        height=300,
        template="plotly_white"
    )

    fig2.update_layout(showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig2, use_container_width=True)
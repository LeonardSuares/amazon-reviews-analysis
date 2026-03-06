import streamlit as st
import plotly.express as px
from utils import load_data

# Page Config
st.set_page_config(layout="wide", page_title="Top Contributing Users")

st.title("🏆 Top Contributing Users")

# 1. Load and Process Data
df = load_data()

# Aggregation logic
recommend_df = df.groupby(['UserId']).agg({
    'Summary': 'count',
    'Score': 'mean',
    'ProductId': 'count'
}).sort_values(by='ProductId', ascending=False)

recommend_df.columns = ['Total Reviews', 'Avg Score', 'Products Purchased']
top_10 = recommend_df.head(10).reset_index()

# 2. Top Reviewers Section
st.subheader("Top 10 Most Active Reviewers")

# Use columns to separate the chart from the raw data table
chart_col, table_col = st.columns([2, 1])

with chart_col:
    # Horizontal bar chart handles UserIDs much better than vertical ones
    fig = px.bar(
        top_10,
        x='Products Purchased',
        y='UserId',
        orientation='h',
        text='Products Purchased',
        color='Products Purchased',
        color_continuous_scale='Teal',
        template='plotly_white',
        height=450
    )

    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},  # Keep highest at the top
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=30, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

with table_col:
    st.markdown("### User Stats")
    # Using st.dataframe instead of st.table for a cleaner, scrollable look
    st.dataframe(
        top_10[['UserId', 'Avg Score', 'Total Reviews']],
        hide_index=True,
        use_container_width=True
    )

st.divider()

# 3. Time Series Section
st.subheader("📅 Review Volume Over Time")

# Resample to yearly counts
df_time = df.set_index('Time').resample('YE')['ProductId'].count().reset_index()
df_time.columns = ['Year', 'Review Count']

# Create a styled Plotly Line Chart
fig_line = px.line(
    df_time,
    x='Year',
    y='Review Count',
    markers=True,
    template='plotly_white',
    color_discrete_sequence=['teal'],
    height=400
)

fig_line.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Reviews",
    margin=dict(l=20, r=20, t=10, b=20)
)

st.plotly_chart(fig_line, use_container_width=True)
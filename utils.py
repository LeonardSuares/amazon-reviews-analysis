import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    """Loads the compressed parquet data and prepares it for analysis."""
    df = pd.read_parquet('data/reviews.parquet')
    # Convert time here so we don't have to do it on every single page
    df['Time'] = pd.to_datetime(df['Time'], unit='s')
    return df
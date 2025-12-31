import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data

st.title("Reviewer Behavior Analysis")
df = load_data()

# Logic: Identify frequent reviewers
user_counts = df['UserId'].value_counts()
df['viewer_type'] = df['UserId'].apply(lambda x: "Frequent" if user_counts[x] > 50 else "Not Frequent")

# Calculate length
df['Text_length'] = df['Text'].apply(lambda x: len(str(x).split(' ')))

st.subheader("Review Length: Frequent vs. Non-Frequent")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Frequent
sns.boxplot(y=df[df['viewer_type']=='Frequent']['Text_length'], ax=ax1, color="skyblue")
ax1.set_title('Frequent Reviewers (>50 reviews)')
ax1.set_ylim(0, 600)

# Non-Frequent
sns.boxplot(y=df[df['viewer_type']=='Not Frequent']['Text_length'], ax=ax2, color="salmon")
ax2.set_title('Non-Frequent Reviewers')
ax2.set_ylim(0, 600)

st.pyplot(fig)

st.info("Frequent reviewers tend to have a more consistent review length compared to casual users.")
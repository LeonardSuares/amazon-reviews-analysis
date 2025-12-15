import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# 1. Shows all columns (You already have this)
pd.set_option('display.max_columns', None)

# 2. DISABLES WRAPPING by setting the display width to a very high number
pd.set_option('display.width', 1000)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

con = sqlite3.connect(r'C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Amazon-dataAnalysis\database.sqlite')

df = pd.read_sql_query("select * from REVIEWS", con)

df_valid = df[df['HelpfulnessNumerator']<=df['HelpfulnessDenominator']]

# print(df_valid.columns)
data = df_valid.drop_duplicates(('UserId', 'ProfileName', 'Time', 'Text'))
data['Time'] = pd.to_datetime(data['Time'], unit = 's')


# print(len(data['ProductId'].unique()))
prod_count = (data['ProductId'].value_counts().reset_index())

prod_ids = prod_count[prod_count['count'] > 500]

freq_prod_ids = prod_ids['ProductId'].values

freq_prod_df = data[data['ProductId'].isin(freq_prod_ids)]
# print(freq_prod_df)
plt.figure(figsize=(10, 16)) # Increased height (16) to accommodate more ProductIds

# 2. Generate the countplot
sns.countplot(
    y='ProductId',
    data=freq_prod_df,
    hue='Score',
    # Use the number of reviews as the color hue for better visual distinction
    order=freq_prod_df['ProductId'].value_counts().index
)

plt.title('Frequency of Products with Over 500 Reviews', fontsize=16)
plt.xlabel('Number of Reviews', fontsize=12)
plt.ylabel('Product ID', fontsize=12)

plt.show()




# print(f"\nTotal unique products before filtering: {len(data['ProductId'].unique())} 🛍️")
# print(f"Total products reviewed more than 500 times: {len(prodtotal.index)} 🌟")
# print("\nTop 10 Most Reviewed Products:")
# print(prodtotal.head(10))

# fre_prod_df = data[data['ProductId'].isin(freq_prod_ids)]

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
# print(data.columns)

recommend_df = data.groupby(['UserId']).agg({'Summary':'count', 'Text':'count', 'Score':'mean', 'ProductId':'count'}).sort_values(by='ProductId', ascending=False)
recommend_df.columns = ['Number_of_summaries', 'num_text','avg_score','No_of_prods_purchased']
# print(recommend_df.index[0:10])
# print(recommend_df['No_of_prods_purchased'][0:10].values)
plt.figure(figsize=(16,7))
plt.bar(recommend_df.index[0:10], recommend_df['No_of_prods_purchased'][0:10].values)
plt.title('Top 10 Users by Number of Products Purchased', fontsize=14)
plt.xlabel('User ID', fontsize=12)
plt.ylabel('Number of Products Purchased', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
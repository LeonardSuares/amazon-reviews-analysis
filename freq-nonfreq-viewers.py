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
# print(data['UserId'].value_counts())
data_count = data['UserId'].value_counts()

# The lambda function must reference the 'data_count' variable, not 'x'.
data['viewer_type'] = data['UserId'].apply(lambda user : "Frequent" if data_count[user] > 50 else "Not Frequent")
# print(data['viewer_type']=='Not Frequent')
not_freq_df = data[data['viewer_type']=='Not Frequent']
freq_df = data[data['viewer_type']=='Frequent']

# freq_df['Score'].value_counts().plot(kind='bar')
# plt.title('Frequent buyers and product scores', fontsize=16)
# plt.xlabel('Scores', fontsize=12)
# plt.ylabel('Count', fontsize=12)
# plt.show()
#
# not_freq_df['Score'].value_counts().plot(kind='bar')
# plt.title('Non-Frequent buyers and product scores', fontsize=16)
# plt.xlabel('Scores', fontsize=12)
# plt.ylabel('Count', fontsize=12)
# plt.show()

# print(len(data['Text'][0].split(' ')))

def calculate_length(text):
    return len(text.split(' '))

data['Text_length'] = data['Text'].apply(calculate_length)
# print(data['viewer_type'].unique())

not_freq_data = data[data['viewer_type']=='Not Frequent']
freq_data = data[data['viewer_type']=='Frequent']

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.boxplot(freq_data['Text_length'])
ax1.set_xlabel('Frequency of frequent reviewers')
ax1.set_ylim(0,600)

ax2 = fig.add_subplot(122)
ax2.boxplot(not_freq_data['Text_length'])
ax2.set_xlabel('Frequency of non-frequent reviewers')
ax2.set_ylim(0,600)

plt.show()
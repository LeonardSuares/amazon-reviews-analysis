import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from textblob import TextBlob
from collections import Counter

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

sample = data[0:50000]

polarity = []

for text in sample['Summary']:
    try:
        polarity.append(TextBlob(text).sentiment.polarity)
    except:
        polarity.append(0)

sample['polarity'] = polarity

sample_negative = sample[sample['polarity']<0]
sample_positive = sample[sample['polarity']>0]

countnegative = Counter(sample_negative['Summary']).most_common(10)
countpositive = Counter(sample_positive['Summary']).most_common(10)

print(countnegative)
print(countpositive)
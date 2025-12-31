import sqlite3
import pandas as pd

con = sqlite3.connect('database.sqlite')
df = pd.read_sql_query("SELECT * FROM REVIEWS", con)
# Initial cleanup to save space
df = df[df['HelpfulnessNumerator'] <= df['HelpfulnessDenominator']]
df.drop_duplicates(('UserId', 'ProfileName', 'Time', 'Text'), inplace=True)
df.to_parquet('data/reviews.parquet', compression='snappy')
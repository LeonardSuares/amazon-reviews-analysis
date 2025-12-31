import sqlite3
import pandas as pd
import os

# 1. Point to your local database
# If the file is in the same folder, just use 'database.sqlite'
db_path = r'C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Amazon-dataAnalysis\database.sqlite'

if not os.path.exists(db_path):
    print("❌ Critical Error: The database file wasn't found at that path.")
else:
    print("Reading database...")
    con = sqlite3.connect(db_path)

    # We use a try-except here to catch the "Table Not Found" error you saw earlier
    try:
        df = pd.read_sql_query("SELECT * FROM REVIEWS", con)

        print("Cleaning data...")
        # Basic cleaning you already wrote
        cols_to_keep = ['UserId', 'ProfileName', 'Time', 'Text', 'Summary',
                        'Score', 'ProductId', 'HelpfulnessNumerator', 'HelpfulnessDenominator']
        df = df[cols_to_keep]

        # 2. Downcast data types (Huge space saver)
        # 'Score' is 1-5, it doesn't need to be a 64-bit float.
        df['Score'] = df['Score'].astype('int8')
        df['HelpfulnessNumerator'] = df['HelpfulnessNumerator'].astype('int32')
        df['HelpfulnessDenominator'] = df['HelpfulnessDenominator'].astype('int32')

        # 3. Optional: Filter out extremely long outlier reviews if you don't need them
        # Or, limit to the top 200,000 rows if you just want to show the functionality
        # df = df.head(200000)

        # 4. Save with "brotli" compression (slower but much tighter than snappy)
        df.to_parquet('data/reviews.parquet', compression='brotli')

        print("✅ Success! 'data/reviews.parquet' is ready.")
        print(f"Original size was large. New size: {os.path.getsize('data/reviews.parquet') / 1024 ** 2:.2f} MB")

    except Exception as e:
        print(f"❌ Error during conversion: {e}")
    finally:
        con.close()
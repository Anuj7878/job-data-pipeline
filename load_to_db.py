import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("jobs_cleaned.csv")

# Connect to database (file create ho jayegi)
conn = sqlite3.connect("jobs.db")

# Save to table
df.to_sql("jobs", conn, if_exists="replace", index=False)

print("Data loaded into database ✅")

# Close connection
conn.close()
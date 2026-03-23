import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("jobs.db")

query = """
SELECT skills, COUNT(*) as count
FROM jobs
GROUP BY skills
ORDER BY count DESC
"""

df = pd.read_sql_query(query, conn)

df.plot(kind='bar', x='skills', y='count')

plt.title("Skills Demand")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
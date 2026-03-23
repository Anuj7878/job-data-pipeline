import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = """
SELECT skills, COUNT(*) as count
FROM jobs
GROUP BY skills
ORDER BY count DESC;
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = """
SELECT skills, COUNT(*) 
FROM jobs 
GROUP BY skills 
ORDER BY COUNT(*) DESC;
"""

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
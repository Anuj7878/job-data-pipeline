import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("jobs.db")

df = pd.read_sql_query("SELECT skills FROM jobs", conn)

# split + clean
df['skills'] = df['skills'].str.split(',')
df = df.explode('skills')
df['skills'] = df['skills'].str.strip()

# count
skill_counts = df['skills'].value_counts().head(10)

# simple colors (clean look)
colors = ['#4E79A7'] * len(skill_counts)
colors[0] = '#E15759'   # highlight top skill

plt.figure()

bars = plt.bar(skill_counts.index, skill_counts.values, color=colors)

# title
plt.title("Top Skills Demand", fontsize=14, fontweight='bold')
plt.xlabel("Skills")
plt.ylabel("Number of Job Listings")

# labels (simple + clean)
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.5,
        int(yval),
        ha='center',
        fontsize=9
    )

plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
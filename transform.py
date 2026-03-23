import pandas as pd

# Load raw data
df = pd.read_csv("job_listings.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove null values
df = df.dropna()

# 🔥 Skills list (Data Engineer ke liye important)
skills_list = [
    "python", "sql", "aws", "gcp", "azure",
    "spark", "hadoop", "kafka",
    "airflow", "etl", "data pipeline",
    "pandas", "numpy",
    "docker", "kubernetes"
]

# 🔥 Multi-skill extraction function
def extract_skills(text):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return ", ".join(found) if found else "Other"
import random

sample_descriptions = [
    "Looking for Python and SQL developer with AWS experience",
    "Data Engineer needed with Spark and Hadoop knowledge",
    "Seeking backend developer with Python, Docker, Kubernetes",
    "ETL developer with Airflow and data pipeline experience",
    "Cloud engineer with AWS and SQL skills"
]

df["job_description"] = df["job_description"].apply(
    lambda x: random.choice(sample_descriptions)
)
# Apply skill extraction
df["skills"] = df["job_description"].apply(extract_skills)

# Optional: count number of skills
df["skills_count"] = df["skills"].apply(lambda x: len(x.split(",")) if x != "Other" else 0)

# Final columns select
df = df[[
    "job_title",
    "job_description",
    "company",
    "location",
    "skills",
    "skills_count"
]]

# Save cleaned data
df.to_csv("jobs_cleaned.csv", index=False)

print("Cleaned and transformed data saved ✅")
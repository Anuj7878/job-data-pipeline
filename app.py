import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Job Data Pipeline Dashboard",
    layout="wide"
)

df = pd.read_csv("jobs_cleaned.csv")

st.title("Job Data Pipeline – Skill Demand Analysis")

total_jobs = len(df)
total_companies = df["company"].nunique()
top_location = df["location"].mode()[0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", total_jobs)
col2.metric("Companies", total_companies)
col3.metric("Top Location", top_location)

st.subheader("Top Skills Demand")

skills_series = df["skills"].dropna().str.split(",")

all_skills = []

for skills in skills_series:
    for skill in skills:
        all_skills.append(skill.strip().lower())

skills_df = pd.Series(all_skills).value_counts().head(10)

fig1 = px.bar(
    x=skills_df.index,
    y=skills_df.values,
    labels={"x": "Skill", "y": "Demand"},
    template="plotly_dark"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Jobs by Location")

location_df = df["location"].value_counts().head(10)

fig2 = px.pie(
    values=location_df.values,
    names=location_df.index,
    hole=0.5,
    template="plotly_dark"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Top Hiring Companies")

company_df = df["company"].value_counts().head(10)

fig3 = px.bar(
    x=company_df.index,
    y=company_df.values,
    labels={"x": "Company", "y": "Jobs"},
    template="plotly_dark"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)
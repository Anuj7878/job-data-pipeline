import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
df = df.rename(columns={"title": "job_title", "body": "job_description"})
df["company"]= "ABC Company"
df["location"]= "jaipur"
df.to_csv("job_listings.csv", index=False)
print("Data saved successfully")


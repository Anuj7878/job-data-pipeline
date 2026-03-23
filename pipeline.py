import os

print("Running pipeline...")

# Step 1: Extract
os.system("python main.py")

# Step 2: Transform
os.system("python transform.py")

# Step 3: Load to DB
os.system("python load_to_db.py")

print("Pipeline completed ✅")
import pandas as pd

# Connecticut labor dataset
url = "https://data.ct.gov/resource/8zbs-9atu.csv?$limit=50000"

# Load dataset into pandas
df = pd.read_csv(url)

# Quick check
print(df.head())
print(df.shape)

# Save locally
df.to_csv("employment_data.csv", index=False)
import pandas as pd
from sqlalchemy import create_engine

# Load the CSV
df = pd.read_csv("employment_data.csv")

# Create SQLite database
engine = create_engine("sqlite:///employment.db")

# Load data into SQL table
df.to_sql("employment", engine, if_exists="replace", index=False)

print("Database created successfully!")
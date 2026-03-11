import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///employment.db")

# Example query: first 10 rows
query = "SELECT * FROM employment LIMIT 10"
df = pd.read_sql(query, engine)
print(df)

# Example aggregation: count records by industry
query2 = """
SELECT industry, COUNT(*) as records
FROM employment
GROUP BY industry
ORDER BY records DESC
"""
df2 = pd.read_sql(query2, engine)
print(df2)
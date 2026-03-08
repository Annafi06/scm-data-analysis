import pandas as pd
import sqlite3
from pathlib import Path

# Paths
DATA_PATH = Path("data/processed/orders_cleaned.csv")
DB_PATH = Path("database/scm.db")

# Load cleaned data
df = pd.read_csv(DATA_PATH)

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)

# Write data to database
df.to_sql("orders", conn, if_exists="replace", index=False)

conn.close()

print("Data successfully loaded into database.")
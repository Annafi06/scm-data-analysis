import pandas as pd
import sqlite3
from pathlib import Path

RAW_DATA = Path("data/raw/orders_raw.csv")
PROCESSED_DATA = Path("data/processed/orders_cleaned.csv")
DB_PATH = Path("database/scm.db")

def extract():
    return pd.read_csv(RAW_DATA)

def transform(df):
    df = df.dropna()
    return df

def load(df):
    PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(PROCESSED_DATA, index=False)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()

def run_pipeline():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL pipeline executed successfully.")

if __name__ == "__main__":
    run_pipeline()
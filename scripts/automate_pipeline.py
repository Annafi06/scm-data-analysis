import pandas as pd

RAW_DATA_PATH = "data/raw/orders_raw.csv"
OUTPUT_PATH = "data/processed/orders_cleaned.csv"

def run_pipeline():
    df = pd.read_csv(RAW_DATA_PATH)
    df = df.drop_duplicates()

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    categorical_cols = df.select_dtypes(include=["object"]).columns
    df[categorical_cols] = df[categorical_cols].fillna("Unknown")

    df.to_csv(OUTPUT_PATH, index=False)

if __name__ == "__main__":
    run_pipeline()

